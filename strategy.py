"""
MOVING-AVERAGE CROSSOVER (50/200 "golden cross"), long-only.

Source: Kakushadze & Serur, "151 Trading Strategies" (SSRN 3247865), Sec 3.13
("two moving averages").

--------------------------------------------------------------------------
THE RULE
--------------------------------------------------------------------------
Every trading day, for every stock in the universe:

    hold it   while its 50-day average price is ABOVE its 200-day average
    sell it   when the 50-day average drops BELOW the 200-day average

All held names get equal weight. The paper leaves the two lengths open;
50/200 is the standard pair and was picked without trying others.

--------------------------------------------------------------------------
UNIVERSE (same as the assay bot, so the backtests are comparable)
--------------------------------------------------------------------------
    price >= $3, 21-day average dollar volume >= $5M, top 490 by liquidity.
    All inputs lagged one day.

--------------------------------------------------------------------------
BACKTEST (2017-2026, Alpaca survivorship-free data, costs included)
--------------------------------------------------------------------------
    CAGR 10.3%   vol 19.4%   Sharpe 0.60   max drawdown -40.3%
    Typically ~220 names. Turnover ~1.5% of the book per day.

Long-only, unlevered, no stop-losses. In a broad sell-off many names cross
below their 200-day average and are sold, so the book partly moves to cash on
its own -- that is the only "risk control" and it is part of the rule.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

NAME = "moving-average"

# ============================ PARAMETERS ==================================
FAST = 50               # days
SLOW = 200              # days

MIN_PRICE = 3.0
MIN_DOLLAR_VOLUME = 5e6
UNIVERSE_SIZE = 490     # most liquid N, ranked point-in-time
# ==========================================================================

DESCRIPTION = (f"{FAST}/{SLOW}-day moving-average crossover, equal weight across "
               f"names in an uptrend, long-only, unlevered")
LONGEST_LOOKBACK = SLOW


def eligible(close, volume, open_=None):
    """Point-in-time tradable set. Everything is lagged one day."""
    adv = (close * volume).rolling(21, min_periods=5).mean().shift(1)
    ok = (close.shift(1) >= MIN_PRICE) & (adv >= MIN_DOLLAR_VOLUME) & close.notna()
    if open_ is not None:
        ok = ok & open_.notna()
    return ok & (adv.rank(axis=1, ascending=False, na_option="keep") <= UNIVERSE_SIZE)


# A moving average needs most of its window, not every day of it. With the
# strict version, ONE missing daily bar -- routine for some names on Yahoo, the
# live data feed -- blanks that stock's 200-day average for the next 200 days
# and silently drops it from the book. The backtest's Alpaca data has no such
# gaps, so tolerating a few keeps live trading the same rule that was tested.
MIN_COVERAGE = 0.9


def in_uptrend(close) -> pd.DataFrame:
    """True where the fast moving average is above the slow one."""
    fast = close.rolling(FAST, min_periods=int(FAST * MIN_COVERAGE)).mean()
    slow = close.rolling(SLOW, min_periods=int(SLOW * MIN_COVERAGE)).mean()
    return (fast > slow) & slow.notna() & fast.notna()


def target_weights(close, volume, open_) -> pd.DataFrame:
    """Full weight history: equal weight over eligible names in an uptrend."""
    hold = in_uptrend(close) & eligible(close, volume, open_)
    w = hold.astype(float)
    return w.div(w.sum(axis=1).replace(0, np.nan), axis=0).fillna(0.0)


def todays_target(close, volume, open_) -> pd.Series:
    """The portfolio to hold right now: ticker -> weight, summing to 1
    (or to 0 if nothing is in an uptrend, i.e. all cash)."""
    w = target_weights(close, volume, open_).iloc[-1]
    return w[w > 1e-6].sort_values(ascending=False)
