## review

This strategy performs poorly in bear markets, although it performs well in bull markets, so it needs to be used with caution.

This strategy uses exit_profit_only, which results in a very high win rate. However, we cannot evaluate the strategy based solely on the win rate; we must consider various other parameters. Additionally, the backtesting period must be sufficiently extensive, taking into account both bull and bear market conditions. If the backtesting performance is poor, the actual performance in live trading will be even worse.

Considering the changes in market conditions, we must ensure that the drawdown is sufficiently small, and the profit from a single trade needs to be around 1%.

## backtest command
```sh
freqtrade backtesting --config user_data/config.json --strategy KamaFama_2  --breakdown  month 
```
## result
```
Result for strategy KamaFama_2
                                               BACKTESTING REPORT
┏━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃       Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃   Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│  PEPE/USDT │     21 │         1.73 │         351.450 │        35.14 │       13:07:00 │   21     0     0   100 │
│   TIA/USDT │     11 │         1.53 │         215.541 │        21.55 │        5:30:00 │   11     0     0   100 │
│    OM/USDT │      9 │         1.24 │         167.474 │        16.75 │        7:30:00 │    9     0     0   100 │
│  BONK/USDT │      6 │         0.94 │         100.661 │        10.07 │        1:27:00 │    6     0     0   100 │
│   IMX/USDT │      9 │         1.04 │          95.283 │         9.53 │        2:12:00 │    9     0     0   100 │
│  AVAX/USDT │      5 │         0.91 │          62.085 │         6.21 │        0:39:00 │    5     0     0   100 │
│   SOL/USDT │      3 │         1.31 │          56.211 │         5.62 │        1:28:00 │    3     0     0   100 │
│   LDO/USDT │      4 │         0.77 │          32.414 │         3.24 │        4:36:00 │    4     0     0   100 │
│   ICP/USDT │      1 │         2.01 │          32.229 │         3.22 │ 1 day, 0:15:00 │    1     0     0   100 │
│  NEAR/USDT │      1 │         1.11 │          21.183 │         2.12 │        0:30:00 │    1     0     0   100 │
│   RAY/USDT │     23 │         0.07 │          20.966 │          2.1 │       17:55:00 │   22     0     1  95.7 │
│   FIL/USDT │      2 │         1.06 │          18.520 │         1.85 │        0:15:00 │    2     0     0   100 │
│   ADA/USDT │      1 │         1.25 │          18.099 │         1.81 │        0:30:00 │    1     0     0   100 │
│    OP/USDT │      3 │         0.56 │          16.133 │         1.61 │        0:38:00 │    3     0     0   100 │
│   ARB/USDT │      1 │         1.04 │          15.820 │         1.58 │        0:15:00 │    1     0     0   100 │
│  AAVE/USDT │      1 │         0.81 │          15.666 │         1.57 │        0:25:00 │    1     0     0   100 │
│   XRP/USDT │      1 │         1.24 │          14.211 │         1.42 │        1:10:00 │    1     0     0   100 │
│   BCH/USDT │      2 │         0.53 │          11.897 │         1.19 │        0:22:00 │    2     0     0   100 │
│   INJ/USDT │      3 │         0.26 │          11.739 │         1.17 │        2:18:00 │    3     0     0   100 │
│   XLM/USDT │      1 │          0.1 │           1.147 │         0.11 │        5:20:00 │    1     0     0   100 │
│   BTC/USDT │      0 │          0.0 │           0.000 │          0.0 │           0:00 │    0     0     0     0 │
│   ETH/USDT │      0 │          0.0 │           0.000 │          0.0 │           0:00 │    0     0     0     0 │
│   BNB/USDT │      0 │          0.0 │           0.000 │          0.0 │           0:00 │    0     0     0     0 │
│  DOGE/USDT │      0 │          0.0 │           0.000 │          0.0 │           0:00 │    0     0     0     0 │
│   TRX/USDT │      0 │          0.0 │           0.000 │          0.0 │           0:00 │    0     0     0     0 │
│  LINK/USDT │      0 │          0.0 │           0.000 │          0.0 │           0:00 │    0     0     0     0 │
│   SUI/USDT │      0 │          0.0 │           0.000 │          0.0 │           0:00 │    0     0     0     0 │
│  SHIB/USDT │      0 │          0.0 │           0.000 │          0.0 │           0:00 │    0     0     0     0 │
│  HBAR/USDT │      0 │          0.0 │           0.000 │          0.0 │           0:00 │    0     0     0     0 │
│   LTC/USDT │      0 │          0.0 │           0.000 │          0.0 │           0:00 │    0     0     0     0 │
│   DOT/USDT │      0 │          0.0 │           0.000 │          0.0 │           0:00 │    0     0     0     0 │
│   UNI/USDT │      0 │          0.0 │           0.000 │          0.0 │           0:00 │    0     0     0     0 │
│   APT/USDT │      0 │          0.0 │           0.000 │          0.0 │           0:00 │    0     0     0     0 │
│   ETC/USDT │      0 │          0.0 │           0.000 │          0.0 │           0:00 │    0     0     0     0 │
│   VET/USDT │      0 │          0.0 │           0.000 │          0.0 │           0:00 │    0     0     0     0 │
│  ALGO/USDT │      0 │          0.0 │           0.000 │          0.0 │           0:00 │    0     0     0     0 │
│  ATOM/USDT │      0 │          0.0 │           0.000 │          0.0 │           0:00 │    0     0     0     0 │
│ THETA/USDT │      0 │          0.0 │           0.000 │          0.0 │           0:00 │    0     0     0     0 │
│   FET/USDT │     14 │        -0.52 │        -115.562 │       -11.56 │        3:32:00 │   13     0     1  92.9 │
│   STX/USDT │     12 │        -1.28 │        -157.255 │       -15.73 │       11:33:00 │   11     0     1  91.7 │
│      TOTAL │    134 │         0.62 │        1005.910 │       100.59 │        8:13:00 │  131     0     3  97.8 │
└────────────┴────────┴──────────────┴─────────────────┴──────────────┴────────────────┴────────────────────────┘
                                         LEFT OPEN TRADES REPORT
┏━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ TOTAL │      0 │          0.0 │           0.000 │          0.0 │         0:00 │    0     0     0     0 │
└───────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                ENTER TAG STATS
┏━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│       buy │     134 │         0.62 │        1005.910 │       100.59 │      8:13:00 │  131     0     3  97.8 │
│     TOTAL │     134 │         0.62 │        1005.910 │       100.59 │      8:13:00 │  131     0     3  97.8 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                 EXIT REASON STATS
┏━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│      exit_1 │   131 │         1.21 │        1840.387 │       184.04 │          4:48:00 │  131     0     0   100 │
│   stop_loss │     3 │       -25.05 │        -834.477 │       -83.45 │ 6 days, 13:05:00 │    0     0     3     0 │
│       TOTAL │   134 │         0.62 │        1005.910 │       100.59 │          8:13:00 │  131     0     3  97.8 │
└─────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                                                        MIXED TAG STATS
┏━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Enter Tag ┃ Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│       buy │      exit_1 │    131 │         1.21 │        1840.387 │       184.04 │          4:48:00 │  131     0     0   100 │
│       buy │   stop_loss │      3 │       -25.05 │        -834.477 │       -83.45 │ 6 days, 13:05:00 │    0     0     3     0 │
│     TOTAL │             │    134 │         0.62 │        1005.910 │       100.59 │          8:13:00 │  131     0     3  97.8 │
└───────────┴─────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────────┴────────────────────────┘
                    MONTH BREAKDOWN
┏━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━┳━━━━━━━┳━━━━━━━━┓
┃      Month ┃ Tot Profit USDT ┃ Wins ┃ Draws ┃ Losses ┃
┡━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━╇━━━━━━━╇━━━━━━━━┩
│ 31/01/2023 │         150.912 │   15 │     0 │      0 │
│ 28/02/2023 │         -125.79 │   15 │     0 │      1 │
│ 31/03/2023 │         -175.85 │   12 │     0 │      1 │
│ 30/04/2023 │          17.721 │    4 │     0 │      0 │
│ 31/05/2023 │         153.733 │    8 │     0 │      0 │
│ 30/06/2023 │         113.528 │    9 │     0 │      0 │
│ 31/07/2023 │          41.257 │    4 │     0 │      0 │
│ 31/08/2023 │        -257.781 │    1 │     0 │      1 │
│ 30/09/2023 │           13.08 │    1 │     0 │      0 │
│ 31/10/2023 │         124.017 │    7 │     0 │      0 │
│ 30/11/2023 │         292.889 │   18 │     0 │      0 │
│ 31/12/2023 │         658.194 │   37 │     0 │      0 │
└────────────┴─────────────────┴──────┴───────┴────────┘
                   SUMMARY METRICS
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                      ┃ Value               ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from            │ 2023-01-01 00:00:00 │
│ Backtesting to              │ 2023-12-30 00:00:00 │
│ Trading Mode                │ Spot                │
│ Max open trades             │ 1                   │
│                             │                     │
│ Total/Daily Avg Trades      │ 134 / 0.37          │
│ Starting balance            │ 1000 USDT           │
│ Final balance               │ 2005.91 USDT        │
│ Absolute profit             │ 1005.91 USDT        │
│ Total profit %              │ 100.59%             │
│ CAGR %                      │ 101.36%             │
│ Sortino                     │ 3.29                │
│ Sharpe                      │ 1.18                │
│ Calmar                      │ 15.70               │
│ Profit factor               │ 2.21                │
│ Expectancy (Ratio)          │ 7.51 (0.03)         │
│ Avg. daily profit %         │ 0.28%               │
│ Avg. stake amount           │ 1180.712 USDT       │
│ Total trade volume          │ 158215.394 USDT     │
│                             │                     │
│ Best Pair                   │ PEPE/USDT 35.14%    │
│ Worst Pair                  │ STX/USDT -15.73%    │
│ Best trade                  │ FET/USDT 6.09%      │
│ Worst trade                 │ STX/USDT -25.14%    │
│ Best day                    │ 76.552 USDT         │
│ Worst day                   │ -290.037 USDT       │
│ Days win/draw/lose          │ 84 / 269 / 3        │
│ Avg. Duration Winners       │ 4:48:00             │
│ Avg. Duration Loser         │ 6 days, 13:05:00    │
│ Max Consecutive Wins / Loss │ 64 / 1              │
│ Rejected Entry signals      │ 286                 │
│ Entry/Exit Timeouts         │ 0 / 0               │
│                             │                     │
│ Min balance                 │ 769.725 USDT        │
│ Max balance                 │ 2005.91 USDT        │
│ Max % of account underwater │ 33.73%              │
│ Absolute Drawdown (Account) │ 33.73%              │
│ Absolute Drawdown           │ 391.791 USDT        │
│ Drawdown high               │ 161.516 USDT        │
│ Drawdown low                │ -230.275 USDT       │
│ Drawdown Start              │ 2023-02-06 02:40:00 │
│ Drawdown End                │ 2023-03-08 03:30:00 │
│ Market change               │ 241.46%             │
└─────────────────────────────┴─────────────────────┘

Backtested 2023-01-01 00:00:00 -> 2023-12-30 00:00:00 | Max open trades : 1
                                                           STRATEGY SUMMARY
┏━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃   Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃             Drawdown ┃
┡━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ KamaFama_2 │    134 │         0.62 │        1005.910 │       100.59 │      8:13:00 │  131     0     3  97.8 │ 391.791 USDT  33.73% │
└────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴──────────────────────┘
```