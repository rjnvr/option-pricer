import yfinance as yf
# Standard library imports
import datetime

# Third party imports
import requests_cache
import matplotlib.pyplot as plt
from pandas_datareader import data as wb



def get_historical_data(ticker, start_date, end_date):
    # Create a Yahoo Finance ticker object
    df = yf.download(ticker, start=start_date, end=end_date)
    return df
    
@staticmethod
def get_columns(data):
    """
    Gets dataframe columns from previously fetched stock data.
    
    Params:
    data: dataframe representing fetched data
    """
    if data is None:
        return None
    return [column for column in data.columns]

@staticmethod
def get_last_price(data, column_name, column_names):
    """
    Returns last available price for specified column from already fetched data.
    
    Params:
    data: dataframe representing fetched data
    column_name: name of the column in dataframe
    """
    if data is None or column_name is None:
        return None
    if column_name not in column_names:
        return None
    return data[column_name].iloc[len(data) - 1]



@staticmethod
def plot_data(data, ticker, column_name):
    """
    Plots specified column values from dataframe.
    
    Params:
    data: dataframe representing fetched data
    column_name: name of the column in dataframe
    """
    try:
        if data is None:
            return
        data[column_name].plot()
        plt.ylabel(f'{column_name}')
        plt.xlabel('Date')
        plt.title(f'Historical data for {ticker} - {column_name}')
        plt.legend(loc='best')
        plt.show()
    except Exception as e:
        print(e)
        return