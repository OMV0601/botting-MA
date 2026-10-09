# Journal

Append-only log of every run. Written by run_daily.py.

2026-09-29T00:48:42+00:00  INFO  === moving-average daily run 2026-09-29 (execute=False) ===
2026-09-29T00:48:42+00:00  WARN  market closed; continuing anyway because this is a dry run (next open 2026-09-29T09:30:00-04:00)
2026-09-29T00:48:43+00:00  INFO  trading Alpaca paper account PA3BW33Q5HH0
2026-09-29T00:48:43+00:00  INFO  account status=ACTIVE equity=$5,000.00 cash=$5,000.00
2026-09-29T00:58:09+00:00  INFO  === moving-average daily run 2026-09-29 (execute=False) ===
2026-09-29T00:58:09+00:00  WARN  market closed; continuing anyway because this is a dry run (next open 2026-09-29T09:30:00-04:00)
2026-09-29T00:58:09+00:00  INFO  trading Alpaca paper account PA3BW33Q5HH0
2026-09-29T00:58:09+00:00  INFO  account status=ACTIVE equity=$5,000.00 cash=$5,000.00
2026-09-29T01:05:07+00:00  INFO  paper endpoint (set ALPACA_LIVE=true for real money)
2026-09-29T01:05:07+00:00  INFO  account permits 4x margin; plan deploys 100.00% of the capital it was handed, so no leverage is used
2026-09-29T01:05:07+00:00  INFO  plan: 0 orders, $0.00 turnover (0.00% of deployed capital), 305 target names
2026-09-29T01:05:07+00:00  INFO  DRY RUN — nothing sent
2026-09-29T06:39:14+00:00  INFO  === moving-average close-of-day summary 2026-09-29 ===
2026-09-29T06:39:15+00:00  INFO  summarising Alpaca paper account PA3BW33Q5HH0
2026-09-29T06:39:15+00:00  INFO  session P&L: +0.00 ($5,000.00 at the open -> $5,000.00 at the close, 391 minute marks)
2026-09-29T06:39:15+00:00  INFO  close-of-day: equity=$5,000.00 positions=$0.00 across 0 names (traded today: False)
2026-09-29T06:39:15+00:00  WARN  close-of-day email did not send; leaving the day open so the later fire retries
2026-09-29T13:31:03+00:00  INFO  === moving-average daily run 2026-09-29 (execute=True) ===
2026-09-29T13:31:03+00:00  INFO  trading Alpaca paper account PA3BW33Q5HH0
2026-09-29T13:31:04+00:00  INFO  account status=ACTIVE equity=$5,000.00 cash=$5,000.00
2026-09-29T13:38:38+00:00  INFO  paper endpoint (set ALPACA_LIVE=true for real money)
2026-09-29T13:38:38+00:00  INFO  account permits 4x margin; plan deploys 100.00% of the capital it was handed, so no leverage is used
2026-09-29T13:38:38+00:00  INFO  plan: 303 orders, $5,000.00 turnover (100.00% of deployed capital), 303 target names
2026-09-29T13:38:38+00:00  INFO    BUY  A      weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  AAL    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  AAPL   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  ABBV   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  ABNB   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  ABT    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  ACGL   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  ADI    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  ADM    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  ADP    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  AFL    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  AJG    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  AKAM   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  ALAB   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  ALL    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  ALLE   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  AMAT   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  AMD    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  AME    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  AMGN   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  AMP    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  AMZN   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  ANET   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  ANF    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  AON    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  APA    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  APD    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  APH    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  APO    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  ARES   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  ARGX   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  ASST   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  ATI    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  AVGO   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  AWK    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  AXON   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  BAC    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  BBY    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  BDX    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  BIIB   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  BKNG   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  BKR    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  BLK    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  BMY    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  BNY    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  BX     weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  C      weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  CAH    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  CASY   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  CAT    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  CB     weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  CBOE   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  CDW    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  CF     weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  CFG    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  CHD    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  CHYM   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  CI     weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  CL     weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  CLSK   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  CNC    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  COF    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  COHR   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  COP    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  CPAY   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  CRL    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  CRM    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  CRWD   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  CSCO   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  CSX    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  CTAS   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  CTVA   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  CVS    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  CVX    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  D      weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  DAL    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  DASH   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  DDOG   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  DE     weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  DELL   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  DGX    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  DHR    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  DLR    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  DLTR   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  DOCN   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  DRI    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  DVN    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  DXCM   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  EBAY   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  ECL    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  EL     weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  ELV    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  EME    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  EMR    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  EOG    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  EQIX   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  ETN    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  ETR    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  EVRG   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  EW     weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  EXPD   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  EXPE   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  EXR    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  F      weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  FANG   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  FAST   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  FCX    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  FDS    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  FDX    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  FFIV   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  FITB   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  FIX    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  FLEX   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  FOXA   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  FSLY   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  FTNT   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  FWONK  weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  GD     weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  GDDY   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  GE     weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  GEN    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  GEV    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  GILD   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  GLW    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  GM     weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  GOOG   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  GOOGL  weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  GPN    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  GRMN   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  GS     weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  GWW    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  HIG    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  HLT    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  HOOD   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  HPE    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  HPQ    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  HST    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  HUM    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  HWM    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  IBKR   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  INCY   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  INTC   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  IP     weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  IQV    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  IRM    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  IT     weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  ITW    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  IVV    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  JBHT   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  JBL    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  JCI    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  JNJ    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  JPM    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  KDP    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  KEY    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  KEYS   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  KHC    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  KLAC   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  KMB    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  KMI    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  KNX    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  KO     weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  KVUE   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  LH     weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  LITE   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  LLY    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  LRCX   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  LYB    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  LYV    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  MA     weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  MAR    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  MCK    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  MCO    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  MDLZ   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  MDT    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  MET    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  MMM    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  MNST   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  MO     weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  MPC    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  MPWR   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  MRK    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  MRNA   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  MRSH   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  MRVL   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  MS     weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  MSFT   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  MSI    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  MTB    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  MTD    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  MTUM   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  MU     weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  MUU    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  MXL    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  NDAQ   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  NEM    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  NOW    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  NSC    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  NTAP   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  NTNX   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  NTRS   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  NUE    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  NVDA   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  ODFL   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  OKE    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  OKTA   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  OMC    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  OVV    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  OXY    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  PANW   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  PAYX   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  PCAR   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  PFE    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  PFG    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  PGR    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  PH     weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  PHM    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  PLD    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  PLTR   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  PM     weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  PNC    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  PPG    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  PRU    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  PSA    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  PSX    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  PWR    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  PYPL   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  Q      weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  QCOM   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  REGN   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  RF     weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  RJF    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  ROK    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  ROP    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  ROST   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  RSG    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  RTX    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  RVTY   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  SBUX   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  SCHB   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  SCHH   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  SCHW   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  SCHX   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  SHW    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  SJM    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  SLB    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  SMCI   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  SNDK   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  SOXL   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  SOXX   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  SPG    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  SPXL   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  STLD   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  STT    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  STX    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  SW     weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  SWKS   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  SYF    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  SYY    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  TECH   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  TER    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  TFC    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  TGT    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  TMO    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  TRGP   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  TRV    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  TSEM   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  TSM    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  TT     weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  TTWO   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  TXN    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  UAL    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  UNH    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  UNP    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  URI    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  USB    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  USFD   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  V      weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  VEEV   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  VLO    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  VMRK   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  VRSN   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  VRT    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  VRTX   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  VTR    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  VZ     weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  WAB    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  WAT    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  WBD    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  WDAY   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  WDC    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  WELL   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  WFC    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  WMB    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  WRB    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  WSM    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  WST    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  XLF    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  XOM    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  XYZ    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  ZBH    weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  ZBRA   weight=0.33% delta=$+16.50
2026-09-29T13:38:38+00:00  INFO    BUY  ZETA   weight=0.33% delta=$+16.50
2026-09-29T13:41:06+00:00  INFO  run recorded in state/last_run.json
2026-09-29T20:02:50+00:00  INFO  === moving-average close-of-day summary 2026-09-29 ===
2026-09-29T20:02:50+00:00  INFO  summarising Alpaca paper account PA3BW33Q5HH0
2026-09-29T20:02:52+00:00  INFO  session P&L: -9.26 ($5,000.00 at the open -> $4,990.74 at the close, 391 minute marks)
2026-09-29T20:02:52+00:00  INFO  close-of-day: equity=$4,989.50 positions=$4,994.46 across 303 names (traded today: True)
2026-09-29T20:02:52+00:00  WARN  close-of-day email did not send; leaving the day open so the later fire retries
2026-09-30T13:31:07+00:00  INFO  === moving-average daily run 2026-09-30 (execute=True) ===
2026-09-30T13:31:07+00:00  INFO  trading Alpaca paper account PA3BW33Q5HH0
2026-09-30T13:31:07+00:00  INFO  account status=ACTIVE equity=$4,997.49 cash=$-4.97
2026-09-30T13:36:53+00:00  INFO  paper endpoint (set ALPACA_LIVE=true for real money)
2026-09-30T13:36:54+00:00  INFO  account permits 4x margin; plan deploys 100.00% of the capital it was handed, so no leverage is used
2026-09-30T13:36:54+00:00  INFO  plan: 5 orders, $83.33 turnover (1.67% of deployed capital), 300 target names
2026-09-30T13:36:54+00:00  INFO    BUY  AVY    weight=0.33% delta=$+16.66
2026-09-30T13:36:54+00:00  INFO    SELL SJM    weight=0.00% delta=$-16.64
2026-09-30T13:36:54+00:00  INFO    SELL PPG    weight=0.00% delta=$-16.40
2026-09-30T13:36:54+00:00  INFO    SELL NTNX   weight=0.00% delta=$-16.99
2026-09-30T13:36:54+00:00  INFO    SELL CI     weight=0.00% delta=$-16.64
2026-09-30T13:36:58+00:00  INFO  run recorded in state/last_run.json
2026-09-30T20:02:49+00:00  INFO  === moving-average close-of-day summary 2026-09-30 ===
2026-09-30T20:02:49+00:00  INFO  summarising Alpaca paper account PA3BW33Q5HH0
2026-09-30T20:02:50+00:00  INFO  session P&L: -41.69 ($4,998.47 at the open -> $4,956.78 at the close, 391 minute marks)
2026-09-30T20:02:50+00:00  INFO  close-of-day: equity=$4,956.29 positions=$4,911.44 across 300 names (traded today: True)
2026-09-30T20:02:50+00:00  WARN  close-of-day email did not send; leaving the day open so the later fire retries
2026-10-01T13:31:07+00:00  INFO  === moving-average daily run 2026-10-01 (execute=True) ===
2026-10-01T13:31:07+00:00  INFO  trading Alpaca paper account PA3BW33Q5HH0
2026-10-01T13:31:07+00:00  INFO  account status=ACTIVE equity=$4,949.01 cash=$44.90
2026-10-01T13:35:22+00:00  INFO  paper endpoint (set ALPACA_LIVE=true for real money)
2026-10-01T13:35:22+00:00  INFO  account permits 4x margin; plan deploys 100.00% of the capital it was handed, so no leverage is used
2026-10-01T13:35:22+00:00  INFO  plan: 8 orders, $132.10 turnover (2.67% of deployed capital), 300 target names
2026-10-01T13:35:22+00:00  INFO    BUY  DIS    weight=0.33% delta=$+16.50
2026-10-01T13:35:22+00:00  INFO    BUY  ICLR   weight=0.33% delta=$+16.50
2026-10-01T13:35:22+00:00  INFO    BUY  IXUS   weight=0.33% delta=$+16.50
2026-10-01T13:35:22+00:00  INFO    BUY  KKR    weight=0.33% delta=$+16.50
2026-10-01T13:35:22+00:00  INFO    SELL ODFL   weight=0.00% delta=$-16.29
2026-10-01T13:35:22+00:00  INFO    SELL ETR    weight=0.00% delta=$-16.63
2026-10-01T13:35:22+00:00  INFO    SELL AON    weight=0.00% delta=$-16.82
2026-10-01T13:35:22+00:00  INFO    SELL VRT    weight=0.00% delta=$-16.38
2026-10-01T13:35:32+00:00  INFO  run recorded in state/last_run.json
2026-10-01T20:02:48+00:00  INFO  === moving-average close-of-day summary 2026-10-01 ===
2026-10-01T20:02:49+00:00  INFO  summarising Alpaca paper account PA3BW33Q5HH0
2026-10-01T20:02:50+00:00  INFO  session P&L: +21.26 ($4,946.98 at the open -> $4,968.24 at the close, 391 minute marks)
2026-10-01T20:02:50+00:00  INFO  close-of-day: equity=$4,967.76 positions=$4,922.68 across 300 names (traded today: True)
2026-10-01T20:02:50+00:00  WARN  close-of-day email did not send; leaving the day open so the later fire retries
2026-10-02T13:31:07+00:00  INFO  === moving-average daily run 2026-10-02 (execute=True) ===
2026-10-02T13:31:07+00:00  INFO  trading Alpaca paper account PA3BW33Q5HH0
2026-10-02T13:31:07+00:00  INFO  account status=ACTIVE equity=$4,994.77 cash=$45.06
2026-10-02T13:38:04+00:00  INFO  paper endpoint (set ALPACA_LIVE=true for real money)
2026-10-02T13:38:04+00:00  INFO  account permits 4x margin; plan deploys 100.00% of the capital it was handed, so no leverage is used
2026-10-02T13:38:04+00:00  INFO  plan: 6 orders, $100.32 turnover (2.01% of deployed capital), 300 target names
2026-10-02T13:38:04+00:00  INFO    BUY  CIBR   weight=0.33% delta=$+16.65
2026-10-02T13:38:04+00:00  INFO    BUY  ICE    weight=0.33% delta=$+16.65
2026-10-02T13:38:04+00:00  INFO    BUY  QRVO   weight=0.33% delta=$+16.65
2026-10-02T13:38:04+00:00  INFO    SELL ALLE   weight=0.00% delta=$-16.56
2026-10-02T13:38:04+00:00  INFO    SELL EME    weight=0.00% delta=$-16.96
2026-10-02T13:38:04+00:00  INFO    SELL AVY    weight=0.00% delta=$-16.86
2026-10-02T13:38:09+00:00  INFO  run recorded in state/last_run.json
2026-10-02T20:02:50+00:00  INFO  === moving-average close-of-day summary 2026-10-02 ===
2026-10-02T20:02:50+00:00  INFO  summarising Alpaca paper account PA3BW33Q5HH0
2026-10-02T20:02:53+00:00  INFO  session P&L: -1.29 ($4,997.15 at the open -> $4,995.86 at the close, 391 minute marks)
2026-10-02T20:02:53+00:00  INFO  close-of-day: equity=$4,996.04 positions=$4,950.80 across 300 names (traded today: True)
2026-10-02T20:02:53+00:00  WARN  close-of-day email did not send; leaving the day open so the later fire retries
2026-10-05T13:31:07+00:00  INFO  === moving-average daily run 2026-10-05 (execute=True) ===
2026-10-05T13:31:08+00:00  INFO  trading Alpaca paper account PA3BW33Q5HH0
2026-10-05T13:31:08+00:00  INFO  account status=ACTIVE equity=$4,997.74 cash=$45.22
2026-10-05T13:36:56+00:00  INFO  paper endpoint (set ALPACA_LIVE=true for real money)
2026-10-05T13:36:57+00:00  INFO  account permits 4x margin; plan deploys 100.00% of the capital it was handed, so no leverage is used
2026-10-05T13:36:57+00:00  INFO  plan: 1 orders, $16.80 turnover (0.34% of deployed capital), 299 target names
2026-10-05T13:36:57+00:00  INFO    SELL CIBR   weight=0.00% delta=$-16.80
2026-10-05T13:36:59+00:00  INFO  run recorded in state/last_run.json
2026-10-06T13:31:09+00:00  INFO  === moving-average daily run 2026-10-06 (execute=True) ===
2026-10-06T13:31:10+00:00  INFO  trading Alpaca paper account PA3BW33Q5HH0
2026-10-06T13:31:10+00:00  INFO  account status=ACTIVE equity=$5,048.30 cash=$61.99
2026-10-06T13:35:30+00:00  INFO  paper endpoint (set ALPACA_LIVE=true for real money)
2026-10-06T13:35:31+00:00  INFO  account permits 4x margin; plan deploys 100.00% of the capital it was handed, so no leverage is used
2026-10-06T13:35:31+00:00  INFO  plan: 5 orders, $70.35 turnover (1.39% of deployed capital), 296 target names
2026-10-06T13:35:31+00:00  INFO    BUY  CIBR   weight=0.34% delta=$+17.06
2026-10-06T13:35:31+00:00  INFO    SELL AKAM   weight=0.00% delta=$-16.70
2026-10-06T13:35:31+00:00  INFO    SELL QRVO   weight=0.00% delta=$-16.94
2026-10-06T13:35:31+00:00  INFO    SELL KMI    weight=0.00% delta=$-16.83
2026-10-06T13:35:31+00:00  INFO    SELL CTVA   weight=0.00% delta=$-2.82
2026-10-06T13:35:37+00:00  WARN  order rejected: QRVO — HTTP Error 422: Unprocessable Entity
2026-10-06T13:35:37+00:00  INFO  run recorded in state/last_run.json
2026-10-06T20:02:51+00:00  INFO  === moving-average close-of-day summary 2026-10-06 ===
2026-10-06T20:02:51+00:00  INFO  summarising Alpaca paper account PA3BW33Q5HH0
2026-10-06T20:02:54+00:00  INFO  session P&L: -2.95 ($5,046.49 at the open -> $5,043.54 at the close, 391 minute marks)
2026-10-06T20:02:54+00:00  INFO  close-of-day: equity=$5,044.23 positions=$4,963.39 across 297 names (traded today: True)
2026-10-06T20:02:54+00:00  WARN  close-of-day email did not send; leaving the day open so the later fire retries
2026-10-07T13:31:07+00:00  INFO  === moving-average daily run 2026-10-07 (execute=True) ===
2026-10-07T13:31:07+00:00  INFO  trading Alpaca paper account PA3BW33Q5HH0
2026-10-07T13:31:07+00:00  INFO  account status=ACTIVE equity=$5,011.49 cash=$80.82
2026-10-07T13:39:14+00:00  INFO  paper endpoint (set ALPACA_LIVE=true for real money)
2026-10-07T13:39:14+00:00  INFO  account permits 4x margin; plan deploys 100.00% of the capital it was handed, so no leverage is used
2026-10-07T13:39:14+00:00  INFO  plan: 13 orders, $217.05 turnover (4.33% of deployed capital), 294 target names
2026-10-07T13:39:14+00:00  INFO    BUY  ADBE   weight=0.34% delta=$+17.05
2026-10-07T13:39:14+00:00  INFO    BUY  VLTO   weight=0.34% delta=$+17.05
2026-10-07T13:39:14+00:00  INFO    BUY  MGM    weight=0.34% delta=$+17.05
2026-10-07T13:39:14+00:00  INFO    BUY  META   weight=0.34% delta=$+17.05
2026-10-07T13:39:14+00:00  INFO    BUY  WTW    weight=0.34% delta=$+17.05
2026-10-07T13:39:14+00:00  INFO    SELL WBD    weight=0.00% delta=$-16.53
2026-10-07T13:39:14+00:00  INFO    SELL QRVO   weight=0.00% delta=$-16.94
2026-10-07T13:39:14+00:00  INFO    SELL PFG    weight=0.00% delta=$-15.69
2026-10-07T13:39:14+00:00  INFO    SELL PHM    weight=0.00% delta=$-15.64
2026-10-07T13:39:14+00:00  INFO    SELL HIG    weight=0.00% delta=$-16.66
2026-10-07T13:39:14+00:00  INFO    SELL IP     weight=0.00% delta=$-15.41
2026-10-07T13:39:14+00:00  INFO    SELL EXR    weight=0.00% delta=$-16.72
2026-10-07T13:39:14+00:00  INFO    SELL CBOE   weight=0.00% delta=$-18.23
2026-10-07T13:39:22+00:00  WARN  order rejected: WBD — HTTP Error 422: Unprocessable Entity
2026-10-07T13:39:22+00:00  WARN  order rejected: QRVO — HTTP Error 422: Unprocessable Entity
2026-10-07T13:39:22+00:00  INFO  run recorded in state/last_run.json
2026-10-07T20:02:43+00:00  INFO  === moving-average close-of-day summary 2026-10-07 ===
2026-10-07T20:02:43+00:00  INFO  summarising Alpaca paper account PA3BW33Q5HH0
2026-10-07T20:02:45+00:00  INFO  session P&L: -4.83 ($5,010.73 at the open -> $5,005.90 at the close, 391 minute marks)
2026-10-07T20:02:45+00:00  INFO  close-of-day: equity=$5,006.40 positions=$4,911.70 across 296 names (traded today: True)
2026-10-07T20:02:45+00:00  WARN  close-of-day email did not send; leaving the day open so the later fire retries
2026-10-08T13:31:05+00:00  INFO  === moving-average daily run 2026-10-08 (execute=True) ===
2026-10-08T13:31:05+00:00  INFO  trading Alpaca paper account PA3BW33Q5HH0
2026-10-08T13:31:05+00:00  INFO  account status=ACTIVE equity=$4,985.70 cash=$94.68
2026-10-08T13:38:55+00:00  INFO  paper endpoint (set ALPACA_LIVE=true for real money)
2026-10-08T13:38:55+00:00  INFO  account permits 4x margin; plan deploys 100.00% of the capital it was handed, so no leverage is used
2026-10-08T13:38:55+00:00  INFO  plan: 11 orders, $184.21 turnover (3.69% of deployed capital), 297 target names
2026-10-08T13:38:55+00:00  INFO    BUY  BAX    weight=0.34% delta=$+16.79
2026-10-08T13:38:55+00:00  INFO    BUY  CTVA   weight=0.34% delta=$+16.79
2026-10-08T13:38:55+00:00  INFO    BUY  COR    weight=0.34% delta=$+16.79
2026-10-08T13:38:55+00:00  INFO    BUY  EME    weight=0.34% delta=$+16.79
2026-10-08T13:38:55+00:00  INFO    BUY  NTNX   weight=0.34% delta=$+16.79
2026-10-08T13:38:55+00:00  INFO    BUY  PTC    weight=0.34% delta=$+16.79
2026-10-08T13:38:55+00:00  INFO    SELL WBD    weight=0.00% delta=$-16.53
2026-10-08T13:38:55+00:00  INFO    SELL TTWO   weight=0.00% delta=$-16.73
2026-10-08T13:38:55+00:00  INFO    SELL QRVO   weight=0.00% delta=$-16.94
2026-10-08T13:38:55+00:00  INFO    SELL PLD    weight=0.00% delta=$-15.86
2026-10-08T13:38:55+00:00  INFO    SELL CASY   weight=0.00% delta=$-17.43
2026-10-08T13:39:01+00:00  WARN  order rejected: WBD — HTTP Error 422: Unprocessable Entity
2026-10-08T13:39:01+00:00  WARN  order rejected: QRVO — HTTP Error 422: Unprocessable Entity
2026-10-08T13:39:01+00:00  INFO  run recorded in state/last_run.json
2026-10-08T20:02:48+00:00  INFO  === moving-average close-of-day summary 2026-10-08 ===
2026-10-08T20:02:49+00:00  INFO  summarising Alpaca paper account PA3BW33Q5HH0
2026-10-08T20:02:51+00:00  INFO  session P&L: +24.19 ($4,984.91 at the open -> $5,009.10 at the close, 391 minute marks)
2026-10-08T20:02:51+00:00  INFO  close-of-day: equity=$5,008.49 positions=$4,963.94 across 299 names (traded today: True)
2026-10-08T20:02:51+00:00  WARN  close-of-day email did not send; leaving the day open so the later fire retries
2026-10-09T13:31:03+00:00  INFO  === moving-average daily run 2026-10-09 (execute=True) ===
2026-10-09T13:31:03+00:00  INFO  trading Alpaca paper account PA3BW33Q5HH0
2026-10-09T13:31:03+00:00  INFO  account status=ACTIVE equity=$5,031.60 cash=$44.55
2026-10-09T13:41:04+00:00  INFO  paper endpoint (set ALPACA_LIVE=true for real money)
2026-10-09T13:41:04+00:00  INFO  account permits 4x margin; plan deploys 100.00% of the capital it was handed, so no leverage is used
2026-10-09T13:41:04+00:00  INFO  plan: 9 orders, $152.86 turnover (3.04% of deployed capital), 294 target names
2026-10-09T13:41:04+00:00  INFO    BUY  FIG    weight=0.34% delta=$+17.11
2026-10-09T13:41:04+00:00  INFO    BUY  GDXJ   weight=0.34% delta=$+17.11
2026-10-09T13:41:04+00:00  INFO    SELL VLTO   weight=0.00% delta=$-17.03
2026-10-09T13:41:04+00:00  INFO    SELL WBD    weight=0.00% delta=$-16.53
2026-10-09T13:41:04+00:00  INFO    SELL WTW    weight=0.00% delta=$-17.40
2026-10-09T13:41:04+00:00  INFO    SELL QRVO   weight=0.00% delta=$-16.94
2026-10-09T13:41:04+00:00  INFO    SELL LYB    weight=0.00% delta=$-17.06
2026-10-09T13:41:04+00:00  INFO    SELL MAR    weight=0.00% delta=$-16.59
2026-10-09T13:41:04+00:00  INFO    SELL EVRG   weight=0.00% delta=$-17.08
2026-10-09T13:41:11+00:00  WARN  order rejected: WBD — HTTP Error 422: Unprocessable Entity
2026-10-09T13:41:11+00:00  WARN  order rejected: QRVO — HTTP Error 422: Unprocessable Entity
2026-10-09T13:41:11+00:00  INFO  run recorded in state/last_run.json
2026-10-09T20:02:46+00:00  INFO  === moving-average close-of-day summary 2026-10-09 ===
2026-10-09T20:02:47+00:00  INFO  summarising Alpaca paper account PA3BW33Q5HH0
2026-10-09T20:02:49+00:00  INFO  session P&L: +11.41 ($5,031.54 at the open -> $5,042.95 at the close, 391 minute marks)
2026-10-09T20:02:49+00:00  INFO  close-of-day: equity=$5,043.40 positions=$4,948.26 across 296 names (traded today: True)
2026-10-09T20:02:49+00:00  WARN  close-of-day email did not send; leaving the day open so the later fire retries
