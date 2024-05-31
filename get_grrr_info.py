#!/usr/bin/env python3

import yfinance as yf

# Get the ticker info for GRRR
grrr = yf.Ticker('GRRR')
info = grrr.info

# Print the business summary to stdout
print(f"Business Summary: {info['longBusinessSummary']}")
