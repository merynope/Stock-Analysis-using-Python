#this ml code takes user input of BSE stock and predicts share prices for next 4 quarters 

import yfinance as yf
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
from datetime import datetime, timedelta

# Function to predict stock prices for the next 4 quarters
def predict_stock_next_quarters(stock_symbol):
    # Fetch historical data from Yahoo Finance
    stock_data = yf.download(stock_symbol + ".BO", start="2010-01-01", end=datetime.today().strftime('%Y-%m-%d'))
    
    # Preprocess data, extract features and target variable
    stock_data['Days'] = (stock_data.index - stock_data.index[0]).days
    X = stock_data[['Days']].values
    y = stock_data['Close'].values
    
    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Create and fit the model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Predict the next 4 quarters (approximately 3 months or 63 trading days per quarter)
    future_days = np.array([[stock_data['Days'].iloc[-1] + i] for i in range(1, 4 * 63 + 1)])
    future_predictions = model.predict(future_days)
    
    # Provide the predicted prices for the next 4 quarters
    next_quarters_predicted_prices = future_predictions.reshape(4, 63)[-4:]  # Extracting last 4 quarters
    
    # Display predicted prices for the next 4 quarters
    for i, quarter_prices in enumerate(next_quarters_predicted_prices, start=1):
        print(f"Predicted closing price for Quarter {i}: {quarter_prices[-1]}")

# Example usage:
stock_symbol = input("Enter the stock symbol from BSE without suffix (e.g., for Reliance Industries, enter RELIANCE): ")
predict_stock_next_quarters(stock_symbol)

