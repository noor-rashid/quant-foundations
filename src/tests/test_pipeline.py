import sys
sys.path.insert(0, "/Users/nrashid/PycharmProjects/PythonProject/PythonProject/quant-foundations/src")
from data.pipeline import get_ohlcv
import pandas as pd

def test_pipeline():
    result = get_ohlcv("src/data", "BTCUSDT", "1d", "2026-01-01", "2026-01-31")
    assert isinstance(result, pd.DataFrame)

