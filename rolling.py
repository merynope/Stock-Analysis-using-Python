"""This code uses the yfinance library to fetch historical stock data from the Bombay Stock Exchange (BSE) 
for a user-inputted stock symbol and start date."""

import yfinance as yf
import matplotlib.pyplot as plt

# Prompt user for BSE stock symbol and start date
stock_symbol = input("Enter the BSE stock symbol (e.g., 'INFY' for Infosys on BSE): ")
start_date = input("Enter the start date (YYYY-MM-DD): ")

# Add '.BO' suffix for BSE stocks
stock_symbol += '.BO'

try:
    # Fetch stock data using yfinance for BSE
    data = yf.download(stock_symbol, start=start_date, end='2023-12-31')
    
    # Display available columns to understand the data structure
    print("Available columns:", data.columns)
    
    # Calculate the 100-day moving average if 'Close' is available in columns
    if 'Close' in data.columns:
        data['100ma'] = data['Close'].rolling(window=100).mean()
        
        # Plotting the stock prices and the moving average
        plt.figure(figsize=(10, 6))
        plt.plot(data['Close'], label='Close')
        plt.plot(data['100ma'], label='100-day Moving Average')
        plt.title(f'{stock_symbol} Stock Price with 100-day Moving Average')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.show()
    else:
        print("Error: 'Close' column not found in the fetched data.")

except Exception as e:
    print(f"Error fetching data: {e}")
