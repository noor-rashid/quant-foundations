# **QUANT FOUNDATIONS**

Working with crypto API data to build tools and analyses that will help build strong foundations in dealing with 
financial time-series data. Built as a learning project to develop quant foundations: data pipelines, statistical analysis, and backtesting.

## Installation 
```bash
pip install -r requirements.txt
```

## Example Usage:
```python

from quant_foundations.pipeline import get_ohlcv
df = get_ohlcv("data/raw", "BTCUSDT", "1d", "2025-01-01", "2025-01-31")
```

## Tests
```bash
PYTHONPATH=src pytest tests/
```