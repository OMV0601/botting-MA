# botting-MA

An automated **moving-average** strategy for an Alpaca **paper** account, $5,000 starting capital.

50/200-day moving-average crossover: hold every stock whose 50-day average price is above its 200-day average, equal weight.

> Not investment advice. A backtest is not a promise; results below come from past data.

## The algorithm

- Every trading day, for each stock compute its **50-day** and **200-day** average price.
- **Hold** it while the 50-day average is above the 200-day average (an uptrend).
- **Sell** it when the 50-day average drops below the 200-day average.
- All held stocks get equal weight. In a broad sell-off many stocks cross below, so the bot moves partly to cash on its own.

**Universe** (the same as the assay bot, so results compare fairly): US stocks priced at $3 or more, trading at least $5M a day, the 490 most liquid, all measured with a one-day lag. Equities only, no crypto.

**Risk:** long-only, no leverage, no shorting, no stop-losses. The whole account is the strategy.
Crossovers react late. They get whipsawed in choppy, sideways markets, and they sell after a drop has already started.

## Backtest

Alpaca data including delisted companies, 2017–2026, with trading costs:

| $5,000 → (2017–2026) | yearly return | worst drop | Sharpe | names held |
|---|---|---|---|---|
| see backtest workflow | **10.3%** | **−40%** | 0.60 | ~220 |

Run it yourself from the **backtest** workflow in the Actions tab, or locally:

```bash
pip install -r requirements.txt
python fetch_data.py --source alpaca --start 2016-01-01 --end 2026-09-25 --n-tickers 4000 --out data/panel
python backtest.py --panel data/panel
```

Source: Kakushadze & Serur, *151 Trading Strategies* (SSRN 3247865), Section 3.13.

## How it runs

Once per trading day at the open, GitHub Actions runs `run_daily.py`:

1. Checks the market is open, and that it hasn't already traded today.
2. Downloads prices, computes today's target from `strategy.py`.
3. Checks safety: paper endpoint, right account, no shorts, no leverage.
4. Sends market orders for the difference, then logs to `journal.md` and emails a summary.

| File | What it does |
|---|---|
| `strategy.py` | **The algorithm.** Nothing else decides what to buy. |
| `run_daily.py` | Daily entrypoint with gates, safety checks and logging. |
| `paper_trade.py` | Alpaca API, price fetch, plan and orders. |
| `preflight.py` | Checks keys, account and clock. Places no orders. |
| `liquidate.py` | Manual "sell everything" (needs `LIQUIDATE` typed in). |
| `backtest.py` | Backtest from $5,000. |
| `core/` | Backtest engine, costs, data loaders (from the assay project). |

## Setup (not done yet)

Nothing trades until these are set. Each bot needs **its own** Alpaca paper account; it refuses to run on the assay bot's account.

1. Create a new Alpaca paper account funded with $5,000.
2. Repo **secrets**: `ALPACA_API_KEY_ID`, `ALPACA_API_SECRET_KEY` (paper keys start with `PK`).
3. Repo **variable**: `ALPACA_ACCOUNT_ID` = that account's number.
4. Run the **preflight** workflow and confirm it's green.
5. Run **daily rebalance** by hand without "execute" (a dry run), and check the plan.
6. Hook up the daily trigger (the same external clock the assay bot uses).

Optional: `RESEND_API_KEY` secret and `NOTIFY_TO` variable for emails.

**Stop trading:** set the variable `TRADING_ENABLED=false`, or add a file named `HALT` to the repo root.
