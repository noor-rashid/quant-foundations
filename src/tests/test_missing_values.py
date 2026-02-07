import pandas as pd
from quant_foundations.validation import find_missing_values
from quant_foundations.fetchers import fetch_ohlcv

def test_missing():
    data = fetch_ohlcv("BTCUSDT", "1d", "2026-01-01", "2026-01-31")
    result = find_missing_values(data)
    assert result.sum() == 0