import yfinance as yf
import mplfinance as mpf

# Prompt user for BSE stock symbol (without suffix), start date, and end date
stock_symbol = input("Enter the BSE stock symbol (e.g., 'INFY' for Infosys on BSE): ")
start_date = input("Enter the start date (YYYY-MM-DD): ")
end_date = input("Enter the end date (YYYY-MM-DD): ")

# Add '.BO' suffix for BSE stocks
stock_symbol += '.BO'

try:
    # Fetch stock data using yfinance for BSE within specified date range
    data = yf.download(stock_symbol, start=start_date, end=end_date)

    # Plotting only the candlestick chart with zoom functionality using mplfinance
    mpf.plot(data, type='candle', title=f'Candlestick Chart for {stock_symbol}',
             ylabel='Price', style='yahoo', mav=(20, 50), figratio=(10, 6),
             show_nontrading=False, tight_layout=True, datetime_format='%Y-%m-%d',
             xrotation=0)

except Exception as e:
    print(f"Error fetching data: {e}")
