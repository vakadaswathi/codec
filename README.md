# Stock Price Predictor using Machine Learning

## 📌 Project Overview

This project predicts stock closing prices using **Linear Regression**, a supervised machine learning algorithm. Historical stock price data is collected using the **Yahoo Finance API (yfinance)**. The model is trained on historical data and predicts stock prices, allowing comparison between actual and predicted values.

## 🎯 Objective

* Predict stock prices using historical market data.
* Learn the basics of regression algorithms in Machine Learning.
* Visualize actual and predicted stock prices.

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-learn
* yFinance

## 📂 Project Structure

```
Stock_Price_Predictor/
│── stock_price_predictor.py
│── README.md
│── requirements.txt
└── output.png
```

## 📊 Dataset

The project downloads historical stock market data directly from Yahoo Finance using the **yfinance** library. No manual dataset download is required.

## ⚙️ Installation

Install the required libraries:

```bash
pip install pandas numpy matplotlib scikit-learn yfinance
```

## ▶️ How to Run

Run the project using:

```bash
python stock_price_predictor.py
```

## 📈 Output

The program:

* Downloads historical stock data.
* Trains a Linear Regression model.
* Predicts stock prices.
* Displays a graph comparing actual and predicted prices.

## 📚 Machine Learning Algorithm

**Linear Regression**

Linear Regression is a supervised learning algorithm used to predict continuous values. In this project, it predicts stock closing prices based on historical data.

## 🚀 Future Improvements

* Use LSTM (Long Short-Term Memory) neural networks for improved prediction.
* Predict multiple stocks simultaneously.
* Build a web application using Flask or Streamlit.
* Add real-time stock price forecasting.

## 👩‍💻 Author

**Vakada Yagna Swathi**

B.Tech Student | Artificial Intelligence & Machine Learning Enthusiast

## 📄 License

This project is created for educational and internship purposes.
