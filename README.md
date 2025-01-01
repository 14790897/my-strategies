# my strategies

## command

```sh
freqtrade hyperopt --hyperopt-loss SharpeHyperOptLossDaily --spaces buy --strategy E0V1E --config user_data/config.json -e 1500 -j 2 --analyze-per-epoch
```

## The optimized parameters are stored in E0V1E.json.

## hyperopt process show

```
                                  ┏━━━━━━━━┳━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                                  ┃ Best   ┃  Epoch ┃ Trades ┃  Win  Draw  Loss  Win% ┃ Avg profit ┃                    Profit ┃ Avg duration ┃ Objective ┃      Max Drawdown (Acct) ┃
                                  ┡━━━━━━━━╇━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━┩
                                  │ * Best │  3/500 │   1225 │ 1126     0    99  91.9 │      0.01% │  -199.500 USDT  (-39.50%) │      4:59:00 │   0.55029 │  781.496 USDT   (74.74%) │
                                  │ * Best │  4/500 │      3 │    2     0     1  66.7 │     -1.45% │   -25.182 USDT   (-4.99%) │      3:37:00 │   0.41138 │                       -- │
                                  │ * Best │  5/500 │   1252 │ 1150     0   102  91.9 │      0.13% │   631.965 USDT  (125.14%) │      4:09:00 │  -0.94139 │ 1376.340 USDT   (62.77%) │
                                  │ * Best │  8/500 │      5 │    4     0     1  80.0 │      1.70% │    43.898 USDT    (8.69%) │      0:35:00 │  -2.07054 │                       -- │
                                  │ * Best │ 10/500 │     11 │    9     0     2  81.8 │      2.21% │   132.756 USDT   (26.29%) │      0:54:00 │  -2.17570 │    2.534 USDT    (0.40%) │
                                  │ * Best │ 22/500 │    442 │  384     0    58  86.9 │      0.62% │  3917.091 USDT  (775.66%) │      3:25:00 │  -2.81709 │ 4528.847 USDT   (67.37%) │
                                  │ Best   │ 41/500 │    312 │  277     0    35  88.8 │      0.92% │ 5130.193 USDT (1,015.88%) │      2:45:00 │  -3.18003 │  704.429 USDT   (21.32%) │
                                  └────────┴────────┴────────┴────────────────────────┴────────────┴───────────────────────────┴──────────────┴───────────┴──────────────────────────┘
Epochs ━━━━━━━━━━━━━━━━━╺━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  49/500  10% • 2:07:29 • 0:00:07
User interrupted..
2024-12-29 19:24:53,706 - freqtrade.optimize.hyperopt.hyperopt - INFO - 49 epochs saved to 'C:\git-program\freqtrade\user_data\hyperopt_results\strategy_hyper_E0V1E_test_2024-12-29_17-16-59.fthypt'.
2024-12-29 19:24:53,903 - freqtrade.optimize.hyperopt_tools - INFO - Dumping parameters to C:\git-program\freqtrade\user_data\strategies\hyper_E0V1E_test.json

Best result:

    41/500:    312 trades. 277/0/35 Wins/Draws/Losses. Avg profit   0.92%. Median profit   1.54%. Total profit 5130.19274320 USDT (1015.88%). Avg duration 2:45:00 min. Objective: -3.180
```
