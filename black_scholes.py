#implementation of the black-scholes model for option pricing

import numpy as np
from scipy.stats import norm

# define vars
r = 0.01
S = 30
K = 40
T = 240/365
sigma = 0.3

def blackScholes(r, S, K, T, sigma, type="C"):
    d1 = (np.log(S/K) + (r + sigma**2/2)*T)/(sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    try:
        if type == "C":
            price = S*norm.cdf(d1, 0, 1) - K*np.exp(-r*T)*norm.cdf(d2, 0, 1)
        elif type == "P":
            price = K*np.exp(-r*T)*norm.cdf(-d2, 0, 1) - S*norm.cdf(-d1, 0, 1)
        return price
    except:
        print("Invalid option type")

    
print("Option Price: ", round(blackScholes(r, S, K, T, sigma, type="C"), 2))