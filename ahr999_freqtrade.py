# --- Do not remove these libs ---
from freqtrade.strategy.interface import IStrategy
from pandas import DataFrame
import talib.abstract as ta
from freqtrade.strategy import CategoricalParameter, DecimalParameter, IntParameter
import numpy as np
import pandas as pd
import os

# --------------------------------
"""
ahr999囤币指标:
计算方式：ahr999指标 =（比特币价格/200日定投成本）*（比特币价格/指数增长估值）。
其中指数成长估值为币价和币龄的拟合结果，本指数拟合方法为每月对历史数据进行拟合。

指标说明：该指标由微博用户ahr999创建，辅助比特币定投用户结合择机策略做出投资决策。 
该指标隐含了比特币短期定投的收益率及比特币价格与预期估值的偏离度。 
从长期来看，比特币价格与区块高度呈现出一定的正相关，同时借助定投方式的优势，短期定投成本大都位于比特币价格之下。 
因此，当比特币价格同时低于短期定投成本和预期估值时增大投资额，能增大用户收益的概率。 
根据指标回测，当指标低于0.45时适合抄底，在0.45和1.2区间内适合定投BTC，高于该区间意味着错过最佳定投时期。
"""


class ahr999(IStrategy):
    INTERFACE_VERSION = 2
    # Optimal timeframe for the strategy
    timeframe = "1d"
    # Stop Loss and ROI
    stoploss = -1  # 100% stoploss
    # minimal_roi = {"0": 1, "80000": 2, "200000": 3}  # 20% ROI
    use_exit_signal = False  # 使用这个可以只在最后一天卖出比特币(忽视退出信号)

    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        # 200日定投成本，假设为过去200日的几何平均值
        dataframe["geomean"] = self.calculate_geomean(dataframe["close"])

        # 指数增长估值计算（自定义方法）
        dataframe["exp_growth_val"] = self.calculate_exp_growth(dataframe)

        # 计算ahr999指标
        dataframe["ahr999"] = (dataframe["close"] / dataframe["geomean"]) * (
            dataframe["close"] / dataframe["exp_growth_val"]
        )
        return dataframe

    def populate_entry_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        # 查找满足ahr999指标低于0.45的情况
        buy_signals = dataframe["ahr999"] < 0.45
        dataframe.loc[buy_signals, ["enter_long", "enter_tag"]] = (1, "ahr<0.45")

        # 打印满足条件的时间、价格和ahr999指标值
        # if buy_signals.any():
        #     for _, row in dataframe[buy_signals].iterrows():
        #         print(
        #             f"Buy Signal: Date={row['date']}, Price={row['close']}, AHR999={row['ahr999']}, Geomean={row['geomean']}"
        #         )
        # 将所有数据保存到文件
        # for _, row in dataframe.iterrows():
        #     print(
        #         f"Signal: Date={row['date']}, Price={row['close']}, AHR999={row['ahr999']}, Geomean={row['geomean']}"
        #     )
        # self.save_signals(dataframe, "ahr999_signals.csv")
        return dataframe

    def populate_exit_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        # 查找满足ahr999指标高于1.2的情况
        sell_signals = dataframe["ahr999"] > 1.2
        dataframe.loc[sell_signals, ["exit_long", "exit_tag"]] = (1, "ahr>1.2")

        # 设置最后一天为卖出信号
        # last_index = dataframe.index[-1]
        # dataframe.loc[dataframe.index == last_index, ["exit_long", "exit_tag"]] = (
        #     1,
        #     "last-day-sell",
        # )
        # 打印满足条件的时间、价格和ahr999指标值
        # if sell_signals.any():
        #     for _, row in dataframe[sell_signals].iterrows():
        #         print(
        #             f"Sell Signal: Date={row['date']}, Price={row['close']}, AHR999={row['ahr999']}, Geomean={row['geomean']}"
        #         )

        return dataframe

    def calculate_geomean(self, prices: DataFrame) -> DataFrame:
        # 确保在创建 Rolling 对象前移除缺失值
        clean_prices = prices.dropna()
        # 创建 Rolling 对象，对每个窗口的价格取对数
        log_prices = np.log(clean_prices)
        # 计算对数值的滚动平均
        rolling_log_means = log_prices.rolling(window=200).mean()
        # 对每个窗口的对数平均值取指数，得到滚动的几何平均
        geomeans = np.exp(rolling_log_means)
        # print("Rolling geomeans calculated.", geomeans)
        return geomeans

    def calculate_exp_growth(self, dataframe: DataFrame) -> DataFrame:
        # 设置比特币的诞生日期为2009年1月3日
        bitcoin_birthdate = pd.to_datetime("2009-01-03 00:00:00+00:00")

        # 确保你的日期列是 datetime 类型
        dataframe["date"] = pd.to_datetime(dataframe["date"])

        # 计算每个日期与比特币诞生日期的差距，结果单位为天
        dataframe["days_since_bitcoin_birth"] = (
            dataframe["date"] - bitcoin_birthdate
        ).dt.total_seconds() / (24 * 3600)
        exp_growth_val = 10 ** (
            5.84 * np.log10(dataframe["days_since_bitcoin_birth"]) - 17.01
        )
        return exp_growth_val

    def save_signals(self, data: DataFrame, filename: str):
        """保存信号数据到 CSV 文件"""
        data.to_csv(filename, mode="w", header=True, index=False)
