#adjusted closing price = shows the stock's price at the end of the day

#the code calculated the average of the adjusted closing price for each day over a 100 day period to see how the stock's price changes over time

import yfinance as yf
import matplotlib.pyplot as plt

# Prompt user for stock symbol and start date
stock_symbol = input("Enter the stock symbol (e.g., 'HDFCBANK' for HDFC Bank on BSE): ")
start_date = input("Enter the start date (YYYY-MM-DD): ")

# Add '.NS' for NSE if not already provided
if not stock_symbol.endswith('.NS'):
    stock_symbol += '.NS'

try:
    # Fetch stock data using yfinance for NSE
    data = yf.download(stock_symbol, start=start_date, end='2023-12-31')
    
    # Calculate the 100-day moving average
    data['100ma'] = data['Adj Close'].rolling(window=100).mean()
    
    # Display the first few rows of the DataFrame with the calculated moving average
    print(data.head())
    
    # Plotting the stock prices and the moving average
    plt.figure(figsize=(10, 6))
    plt.plot(data['Adj Close'], label='Adj Close')
    plt.plot(data['100ma'], label='100-day Moving Average')
    plt.title(f'{stock_symbol} Stock Price with 100-day Moving Average')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()

except Exception as e:
    print(f"Error fetching data: {e}")

