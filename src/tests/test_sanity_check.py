from quant_foundations.fetchers import fetch_ohlcv
from quant_foundations.validation import sanity_check_values

def test_sanity_check():
    data = fetch_ohlcv("BTCUSDT", "1d", "2026-01-01", "2026-01-31")
    result = sanity_check_values(data)
    assert result["high_low_violations"].empty
    assert result["close_range_anomalies"].empty
    assert result["negative_prices"].empty

