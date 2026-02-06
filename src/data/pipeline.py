import os
from pathlib import Path
import datetime
from data.fetchers import fetch_ohlcv
import pandas as pd

def get_ohlcv(output_dir: str, symbol: str, interval: str, start: str, end: str) -> pd.DataFrame:
    """
    check if cache exists and call if it does, or make API request if not

    :param symbol:
    :param interval:
    :param start:
    :param end:
    :return:
    """
    filename = f"binance_daily_data_{symbol}_{interval}_{start}_{end}.csv"
    filepath = Path(output_dir) / filename

    if not os.path.exists(filepath):
        print("Filepath does not exist, hitting API Endpoint and fetching new data")
        data = fetch_ohlcv(symbol, interval, start, end)
        save_data = data.to_csv(filepath, index=False)
        return data
    else:
        print("Filepath Exists, fetching cached data")
        data = pd.read_csv(filepath)
        return data



