## model architecture is dafault
## It is recommended to increase the number of train_cycles to improve the results.
## backtest command
```sh
freqtrade backtesting --strategy freqai_rl_test_strat --config user_data/config_freqai.json --freqaimodel ReinforcementLearner  
```
## result
```
Result for strategy freqai_rl_test_strat
                                                BACKTESTING REPORT
┏━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃          Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ BTC/USDT:USDT │   1309 │        -0.09 │       -2454.943 │       -30.69 │      2:33:00 │  487     0   822  37.2 │
│         TOTAL │   1309 │        -0.09 │       -2454.943 │       -30.69 │      2:33:00 │  487     0   822  37.2 │
└───────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
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
│      long │    1309 │        -0.09 │       -2454.943 │       -30.69 │      2:33:00 │  487     0   822  37.2 │
│     TOTAL │    1309 │        -0.09 │       -2454.943 │       -30.69 │      2:33:00 │  487     0   822  37.2 │
└───────────┴─────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                               EXIT REASON STATS
┏━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│         roi │   686 │        -0.03 │        -376.543 │        -4.71 │      4:00:00 │  285     0   401  41.5 │
│   stop_loss │     8 │        -5.11 │        -808.335 │        -10.1 │      2:46:00 │    0     0     8     0 │
│ exit_signal │   615 │         -0.1 │       -1270.065 │       -15.88 │      0:56:00 │  202     0   413  32.8 │
│       TOTAL │  1309 │        -0.09 │       -2454.943 │       -30.69 │      2:33:00 │  487     0   822  37.2 │
└─────────────┴───────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                                                             MIXED TAG STATS
┏━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃               Enter Tag ┃ Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│         ('long', 'roi') │             │    686 │        -0.03 │        -376.543 │        -4.71 │      4:00:00 │  285     0   401  41.5 │
│   ('long', 'stop_loss') │             │      8 │        -5.11 │        -808.335 │        -10.1 │      2:46:00 │    0     0     8     0 │
│ ('long', 'exit_signal') │             │    615 │         -0.1 │       -1270.065 │       -15.88 │      0:56:00 │  202     0   413  32.8 │
│                   TOTAL │             │   1309 │        -0.09 │       -2454.943 │       -30.69 │      2:33:00 │  487     0   822  37.2 │
└─────────────────────────┴─────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┘
                    SUMMARY METRICS
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                      ┃ Value                 ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━┩
│ Backtesting from            │ 2021-05-02 01:00:00   │
│ Backtesting to              │ 2023-07-30 00:00:00   │
│ Trading Mode                │ Isolated Futures      │
│ Max open trades             │ 1                     │
│                             │                       │
│ Total/Daily Avg Trades      │ 1309 / 1.6            │
│ Starting balance            │ 8000 USDT             │
│ Final balance               │ 5545.057 USDT         │
│ Absolute profit             │ -2454.943 USDT        │
│ Total profit %              │ -30.69%               │
│ CAGR %                      │ -15.09%               │
│ Sortino                     │ -3.82                 │
│ Sharpe                      │ -2.83                 │
│ Calmar                      │ -2.33                 │
│ Profit factor               │ 0.72                  │
│ Expectancy (Ratio)          │ -1.88 (-0.18)         │
│ Avg. daily profit %         │ -0.04%                │
│ Avg. stake amount           │ 1983.545 USDT         │
│ Total trade volume          │ 2596460.323 USDT      │
│                             │                       │
│ Best Pair                   │ BTC/USDT:USDT -30.69% │
│ Worst Pair                  │ BTC/USDT:USDT -30.69% │
│ Best trade                  │ BTC/USDT:USDT 10.00%  │
│ Worst trade                 │ BTC/USDT:USDT -5.13%  │
│ Best day                    │ 227.891 USDT          │
│ Worst day                   │ -186.85 USDT          │
│ Days win/draw/lose          │ 71 / 496 / 124        │
│ Avg. Duration Winners       │ 2:49:00               │
│ Avg. Duration Loser         │ 2:24:00               │
│ Max Consecutive Wins / Loss │ 8 / 30                │
│ Rejected Entry signals      │ 0                     │
│ Entry/Exit Timeouts         │ 0 / 0                 │
│                             │                       │
│ Min balance                 │ 5542.746 USDT         │
│ Max balance                 │ 8008.137 USDT         │
│ Max % of account underwater │ 30.79%                │
│ Absolute Drawdown (Account) │ 30.79%                │
│ Absolute Drawdown           │ 2465.391 USDT         │
│ Drawdown high               │ 8.137 USDT            │
│ Drawdown low                │ -2457.254 USDT        │
│ Drawdown Start              │ 2021-08-01 04:05:00   │
│ Drawdown End                │ 2023-06-19 12:10:00   │
│ Market change               │ 1.16%                 │
└─────────────────────────────┴───────────────────────┘

Backtested 2021-05-02 01:00:00 -> 2023-07-30 00:00:00 | Max open trades : 1
                                                                STRATEGY SUMMARY
┏━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━┓
┃             Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃ Avg Duration ┃  Win  Draw  Loss  Win% ┃              Drawdown ┃
┡━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━┩
│ freqai_rl_test_strat │   1309 │        -0.09 │       -2454.943 │       -30.69 │      2:33:00 │  487     0   822  37.2 │ 2465.391 USDT  30.79% │
└──────────────────────┴────────┴──────────────┴─────────────────┴──────────────┴──────────────┴────────────────────────┴───────────────────────┘
```