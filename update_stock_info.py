#!/usr/bin/env python
import csv
import yfinance as yf
import datetime

# Import the list of tickers
with open('tickers.txt', 'r') as file:
    for line in file:
        # Get the ticker symbol
        ticker = line.strip()
        
        # Get the ticker data
        data = yf.Ticker(ticker)
        
        # Get the ticker info
        info = data.info
        
        # Get the current date
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")

        # Create the file name with current date
        file_name = f'stock_info_{current_date}.csv'

        # Print the ticker info into the new CSV file
        with open(file_name, 'a') as file:
            writer = csv.writer(file)
            
            # Add header row if file is empty
            if file.tell() == 0:
                writer.writerow(['Name', 'Symbol', 'Sector', 'Industry', 'Market Cap', 'Current Price', 'Volume', 'Investor Website', 'Enterprise Value', 'Trailing EPS', 'Forward EPS', 'Dividend Yield', 'Price to Book', 'Enterprise to EBITDA', 'Return on Assets', 'Return on Equity'])
            
            writer.writerow([
            info.get('shortName', 'N/A'),
            info.get('symbol', 'N/A'),
            info.get('sector', 'N/A'),
            info.get('industry', 'N/A'),
            info.get('marketCap', 'N/A'),
            info.get('currentPrice', 'N/A'),
            info.get('regularMarketVolume', 'N/A'),
            info.get('website', 'N/A'),
            info.get('enterpriseValue', 'N/A'),
            info.get('trailingEps', 'N/A'),
            info.get('forwardEps', 'N/A'),
            info.get('dividendYield', 'N/A'),
            info.get('priceToBook', 'N/A'),
            info.get('enterpriseToEbitda', 'N/A'),
            info.get('returnOnAssets', 'N/A'),
            info.get('returnOnEquity', 'N/A')
            ])

            # Remove empty rows from the output file
            with open(file_name, 'r+') as file:
                lines = file.readlines()
                file.seek(0)
                for line in lines:
                    if line.strip():
                        file.write(line)
                file.truncate()