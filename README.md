
# Time Series Financial Forecasting

## Overview
This project utilizes historical financial data to forecast future trends using time series models, specifically ARIMA and Prophet. The focus is on predicting financial metrics such as the `Price` of stocks over time.

## Features
- **Data Preprocessing**: Aggregated numeric data and created a synthetic time index for analysis.
- **Exploratory Data Analysis (EDA)**: Visualized financial trends and patterns over time.
- **Forecasting**:
  - ARIMA Model: Used for linear time series forecasting.
  - Prophet Model: Captures trends and seasonality in the data.

## Dataset
The dataset was sourced from the [S&P 500 Companies with Financial Information](https://www.kaggle.com/datasets/paytonfisher/sp-500-companies-with-financial-information).

## Results
### ARIMA Model
- **RMSE**: Noted for linear time series forecasting.
- **Key Findings**: ARIMA effectively modeled short-term linear trends in the data.

### Prophet Model
- **RMSE**: 251.46
- **Key Findings**: Prophet identified non-linear trends and provided a seasonal decomposition for financial data.

## Visualizations
- Line plots for actual vs. predicted values using ARIMA and Prophet.
- Prophet's seasonal decomposition components.

## Technologies Used
- Python
- Pandas, NumPy
- Statsmodels (ARIMA)
- Prophet
- Matplotlib, Seaborn

## How to Run
1. Clone this repository.
2. Install required dependencies:
   ```bash
   pip install pandas numpy matplotlib seaborn statsmodels prophet
   ```
3. Run the Python script:
   ```bash
   python financial_forecasting.py
   ```

## Limitations
- The dataset was synthetically adjusted for time series analysis due to the absence of a natural time index.
- Models may require further tuning for more complex patterns.

## Future Work
- Incorporate external factors such as market indices for more accurate predictions.
- Experiment with additional time series models such as LSTM.
