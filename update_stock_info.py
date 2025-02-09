#!/usr/bin/env python
import yfinance as yf
import json
import time

# Filenames
json_filename = 'stock_data.json'
tickers_filename = 'tickers.txt'
processed_filename = 'processed_ticker.txt'

def load_json_data(filename):
    """Load existing JSON data or return an empty dictionary if the file doesn't exist or is invalid."""
    try:
        with open(filename, 'r') as jf:
            return json.load(jf)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_json_data(filename, data):
    """Save the data dictionary to a JSON file."""
    with open(filename, 'w') as jf:
        json.dump(data, jf, indent=4)

# Load any previously processed stock data from JSON
stock_data = load_json_data(json_filename)

# Read the list of tickers from tickers.txt
with open(tickers_filename, 'r') as file:
    tickers = [line.strip() for line in file if line.strip()]

# Process each ticker one by one
for ticker in tickers:
    try:
        print(f"Processing ticker: {ticker}")
        stock = yf.Ticker(ticker)
        info = stock.info  # This is the API call that might trigger rate limiting
        
        # Update the stock_data dictionary with the new information
        stock_data[ticker] = info
        
        # Save the updated data to the JSON file immediately
        save_json_data(json_filename, stock_data)
        
        # Log the processed ticker so you have a record of which ones are done
        with open(processed_filename, 'a') as processed_file:
            processed_file.write(f"{ticker}\n")
        
        # Remove the processed ticker from tickers.txt
        # Read in the current tickers, filter out the processed ticker, and overwrite the file.
        with open(tickers_filename, 'r') as tf:
            lines = tf.readlines()
        with open(tickers_filename, 'w') as tf:
            for line in lines:
                if line.strip() != ticker:
                    tf.write(line)
                    
    except Exception as e:
        # If an error occurs (like a rate limit error), print the error,
        # optionally wait before retrying, and then break out of the loop.
        print(f"Error processing {ticker}: {e}")
        # Optional: Wait a minute before exiting if you expect a temporary rate-limit.
        time.sleep(60)
        break

print("Processing complete or interrupted by an error.")