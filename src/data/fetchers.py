import time
import pandas as pd
import httpx

def fetch_ohlcv(symbol: str, interval: str, start: str, end: str) -> pd.DataFrame:
    """
    Fetch OHLCV data from Binance API

    :param symbol: ticker symbol, e.g "BTCUSDT"
    :param interval: e.g "1h", "1d"
    :param start: ISO date string e.g. "2025-01-01"
    :param end:
    :return: DataFrame with OHLCV data
    """
    start = pd.to_datetime(start)
    end = pd.to_datetime(end)
    start_mil = int(time.mktime(start.timetuple()) * 1000)
    end_mil = int(time.mktime(end.timetuple()) * 1000)

    params = {"symbol":symbol, "interval":interval, "startTime":start_mil, "endTime":end_mil}
    r = httpx.get("https://api.binance.com/api/v3/klines", params=params)
    content = r.json()
    columns = ["openTime", "Open", "High", "Low", "Close", "Volume", "closeTime", "quoteAssetVol", "num_trades", "TakerBaseAssetVol", "TakerBuyQuoteAssetVol", "0"]
    data = pd.DataFrame(content, columns=columns)
    data["openTime"] = pd.to_datetime(data["openTime"], unit="ms")
    data["closeTime"] = pd.to_datetime(data["closeTime"], unit="ms")
    float_cols = ["Open", "High", "Low", "Close", "Volume", "TakerBaseAssetVol", "TakerBuyQuoteAssetVol"]
    int_cols = ["num_trades"]
    data[float_cols] = data[float_cols].astype("float64")
    data[int_cols] = data[int_cols].astype("int64")

    return data