#implementation of the black-scholes model for option pricing
import streamlit as st
import numpy as np
from scipy.stats import norm
from datetime import datetime, timedelta

def calculate_call_option_price(underlying_spot_price, strike_price, days_to_maturity, risk_free_rate, sigma): 
        """
        Calculates price for call option according to the formula.        
        Formula: S*N(d1) - PresentValue(K)*N(d2)
        """
        S = underlying_spot_price
        K = strike_price
        T = days_to_maturity / 365
        r = risk_free_rate
        # cumulative function of standard normal distribution (risk-adjusted probability that the option will be exercised)     
        d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
        
        # cumulative function of standard normal distribution (probability of receiving the stock at expiration of the option)
        d2 = (np.log(S / K) + (r - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
        
        return (S * norm.cdf(d1, 0.0, 1.0) - K * np.exp(-r * T) * norm.cdf(d2, 0.0, 1.0))
    
def calculate_put_option_price(underlying_spot_price, strike_price, days_to_maturity, risk_free_rate, sigma): 
    """
    Calculates price for put option according to the formula.        
    Formula: PresentValue(K)*N(-d2) - S*N(-d1)
    """  
    S = underlying_spot_price
    K = strike_price
    T = days_to_maturity / 365
    r = risk_free_rate
    # cumulative function of standard normal distribution (risk-adjusted probability that the option will be exercised)    
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))

    # cumulative function of standard normal distribution (probability of receiving the stock at expiration of the option)
    d2 = (np.log(S / K) + (r - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    
    return (K * np.exp(-r * T) * norm.cdf(-d2, 0.0, 1.0) - S * norm.cdf(-d1, 0.0, 1.0))




