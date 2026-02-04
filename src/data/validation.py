import pandas as pd

def timestamp_difference(df: pd.DataFrame, start: str, end: str) -> pd.DatetimeIndex:

    """

    :param star:
    :param end:
    :return:
    """
    return pd.date_range(start=start, end=end).difference(df.index)

def find_missing_values(df: pd.DataFrame) -> pd.Series:
    """

    :param df:
    :return:
    """

    return df.isnull().sum().sort_values()

def sanity_check_values(df: pd.DataFrame) -> dict:
    """

    :param df:
    :return:
    """
    high_low_diff = df["High"] >= df["Low"]
    close_between_low_high = (df["Close"] >= df["Low"]) & (df["Close"] <= df["High"])
    price_positive = (df["Open"] > 0) & (df["Close"] > 0)

    high_anomaly = df.loc[high_low_diff==False]
    close_anomaly = df.loc[close_between_low_high==False]
    price_anomaly = df.loc[price_positive==False]

    return {
        "high_low_violations": high_anomaly,
        "close_range_anomalies": close_anomaly,
        "negative_prices": price_anomaly
    }