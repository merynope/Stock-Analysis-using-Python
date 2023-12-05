"""this is a python script that allows users to input a stock symbol, start date, 
and end date to visualize the historical stock prices for that symbol within the specified date range."""
import yfinance as yf
import matplotlib.pyplot as plt

# Prompt user for stock symbol (from BSE)
stock_symbol = input("Enter the stock symbol from BSE (e.g., 'NTPC'): ")

# Prompt user for start date
start_date = input("Enter the start date (YYYY-MM-DD): ")

# Prompt user for end date
end_date = input("Enter the end date (YYYY-MM-DD): ")

# Fetch data using yfinance based on user input
df = yf.download(stock_symbol + '.NS', start=start_date, end=end_date)

# Plotting the 'Close' prices
plt.figure(figsize=(10, 6))
plt.plot(df['Close'], label=stock_symbol)
plt.title(f'{stock_symbol} Stock Price Visualization')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()
