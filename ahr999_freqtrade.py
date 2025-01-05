# --- Do not remove these libs ---
from freqtrade.strategy.interface import IStrategy
from pandas import DataFrame
import talib.abstract as ta
from freqtrade.strategy import CategoricalParameter, DecimalParameter, IntParameter
import numpy as np
import pandas as pd
import os

# --------------------------------


class ahr999(IStrategy):
    INTERFACE_VERSION = 2
    # Optimal timeframe for the strategy
    timeframe = "1d"
    # Stop Loss and ROI
    stoploss = -2  # 200% stoploss
    # minimal_roi = {"0": 1, "80000": 2, "200000": 3}  # 20% ROI

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
        dataframe.loc[buy_signals, "buy"] = 1

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
        dataframe.loc[sell_signals, "sell"] = 1

        # 设置最后一天为卖出信号
        last_index = dataframe.index[-1]
        dataframe.loc[dataframe.index == last_index, "sell"] = 1
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
        data.to_csv(
            filename, mode="w", header=not os.path.exists(filename), index=False
        )
