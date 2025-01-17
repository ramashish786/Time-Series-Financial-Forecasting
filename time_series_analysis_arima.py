# -*- coding: utf-8 -*-
"""Time Series Analysis - ARIMA.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1rrerYtnEMTBxvFWzQwvxEYBHW4AfSqce
"""

import kagglehub

# Download latest version
path = kagglehub.dataset_download("paytonfisher/sp-500-companies-with-financial-information")

print("Path to dataset files:", path)

df = pd.read_csv(file_path)

import kagglehub
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
from math import sqrt
from prophet import Prophet

df.columns

# Keep only numeric columns and Symbol for aggregation
numeric_columns = df.select_dtypes(include=[np.number]).columns
df = df[["Symbol"] + list(numeric_columns)]

# Aggregate by Symbol and select the "Price" column
df = df.groupby("Symbol").mean().reset_index()
df = df[["Symbol", "Price"]]

# Sort for synthetic time ordering
df = df.sort_values(by="Price").reset_index(drop=True)
df["date"] = pd.date_range(start="2020-01-01", periods=len(df), freq="M")

# Select relevant columns for time series analysis
df = df[["date", "Price"]].rename(columns={"Price": "value"})

# Plot the value data
plt.figure(figsize=(10, 6))
plt.plot(df["date"], df["value"], label="Value")
plt.title("Value Over Time")
plt.xlabel("Date")
plt.ylabel("Value")
plt.legend()
plt.show()

# Split into training and testing sets
train_size = int(len(df) * 0.8)
train, test = df[:train_size], df[train_size:]

# ARIMA Model
print("\nARIMA Model")
arima_model = ARIMA(train["value"], order=(5, 1, 0))
arima_fit = arima_model.fit()
print(arima_fit.summary())

# Make predictions
arima_forecast = arima_fit.forecast(steps=len(test))
rmse_arima = sqrt(mean_squared_error(test["value"], arima_forecast))
print(f"ARIMA RMSE: {rmse_arima}")

# Plot ARIMA predictions
plt.figure(figsize=(10, 6))
plt.plot(train["date"], train["value"], label="Train")
plt.plot(test["date"], test["value"], label="Test")
plt.plot(test["date"], arima_forecast, label="ARIMA Forecast")
plt.title("ARIMA Forecast vs Actual")
plt.xlabel("Date")
plt.ylabel("Value")
plt.legend()
plt.show()

# Prophet Model
print("\nProphet Model")
prophet_data = df.rename(columns={"date": "ds", "value": "y"})
prophet_train = prophet_data[:train_size]
prophet_test = prophet_data[train_size:]

# Train Prophet model
prophet_model = Prophet()
prophet_model.fit(prophet_train)

# Make predictions
future = prophet_model.make_future_dataframe(periods=len(test), freq="M")
forecast = prophet_model.predict(future)

# Extract predicted values for test range
prophet_forecast = forecast.loc[forecast["ds"].isin(prophet_test["ds"]), "yhat"].values
rmse_prophet = sqrt(mean_squared_error(test["value"], prophet_forecast))
print(f"Prophet RMSE: {rmse_prophet}")

# Plot Prophet predictions
plt.figure(figsize=(10, 6))
plt.plot(train["date"], train["value"], label="Train")
plt.plot(test["date"], test["value"], label="Test")
plt.plot(test["date"], prophet_forecast, label="Prophet Forecast")
plt.title("Prophet Forecast vs Actual")
plt.xlabel("Date")
plt.ylabel("Value")
plt.legend()
plt.show()

# Prophet Forecast Components
prophet_model.plot_components(forecast)
plt.show()