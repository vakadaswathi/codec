import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Download stock data
data = yf.download("AAPL", start="2023-01-01", end="2024-01-01")

# Use day number as feature
data = data.reset_index()
data["Day"] = range(len(data))

X = data[["Day"]]
y = data["Close"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Predict prices
data["Predicted"] = model.predict(X)

# Plot
plt.figure(figsize=(10,5))
plt.plot(data["Close"], label="Actual Price")
plt.plot(data["Predicted"], label="Predicted Price")
plt.xlabel("Days")
plt.ylabel("Stock Price")
plt.title("Stock Price Prediction")
plt.legend()
plt.show()