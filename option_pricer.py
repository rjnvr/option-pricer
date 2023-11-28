#implementation of the black-scholes model for option pricing
import streamlit as st
import numpy as np
import black_scholes
import functions
from scipy.stats import norm
from datetime import datetime, timedelta

option_method = ['Call', 'Put']
# default vars
available_pricing_methods = ['Black-Scholes']
pricing_method = st.sidebar.selectbox('Select pricing method', available_pricing_methods)


# Ignore the Streamlit warning for using st.pyplot()
st.set_option('deprecation.showPyplotGlobalUse', False)

# Main title
st.title('Option pricing')

st.subheader(f'Pricing method: {pricing_method}')

method_selected = st.selectbox('Select Option method', option_method)

# if pricing method is black scholes
if pricing_method == 'Black-Scholes':
    #Parameters for Black-Scholes model
    ticker = st.text_input('Ticker symbol', 'AAPL')
    strike_price = st.number_input('Strike price', 300)
    risk_free_rate = st.slider('Risk-free rate (%)', 0, 100, 10)
    sigma = st.slider('Sigma (%)', 0, 100, 20)
    exercise_date = st.date_input('Exercise date', min_value=datetime.today() + timedelta(days=1), value=datetime.today() + timedelta(days=365))

    if st.button(f'Calculate option price for {ticker}'):
        # Getting data for selected ticker
        data = functions.get_historical_data(ticker, datetime.today() - timedelta(365), datetime.today())
        st.write(data.tail())
        functions.plot_data(data, ticker, 'Adj Close')
        st.pyplot()

        # Formating selected model parameters
        spot_price = functions.get_last_price(data, 'Adj Close', functions.get_columns(data)) 
        risk_free_rate = risk_free_rate / 100
        sigma = sigma / 100
        days_to_maturity = (exercise_date - datetime.now().date()).days

        # Calculating option price
        if method_selected == option_method[0]:
            call_option_price = black_scholes.calculate_call_option_price(spot_price, strike_price, days_to_maturity, risk_free_rate, sigma)
            st.subheader(f'Call option price: {call_option_price}')
        else:
            put_option_price = black_scholes.calculate_put_option_price(spot_price, strike_price, days_to_maturity, risk_free_rate, sigma)
            st.subheader(f'Put option price: {put_option_price}')
