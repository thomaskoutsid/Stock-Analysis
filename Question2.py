'''
Thomas Koutsidis
7/8/22
Question 2
Program that calculates relative standard deviation for eight Dow Jones companies.
'''

import pandas as pd
import yfinance as yf


def rel_std(stock_data):
    
    #calculates and returns relative standard deviation 
    sum = 0
    m, n = stock_data.shape
    for x in stock_data["Close"]:
        sum += x
    x_hat = sum / m
    
    sum_sq = 0
    for x in stock_data["Close"]:
        sum_sq += (x - x_hat)**2
    var = sum_sq / (m - 1)
    
    std = var ** (1/2)
    
    relstd = (std / x_hat) * 100
    
    return relstd
    
    
def main():
    
    #downloaded 8 Dow Jones stocks
    symbols = ['ba', 'ko', 'xom', 'ge', 'jpm', 'nke', 'pfe', 'vz' ]
    arr = []
    for i in symbols:
        df = yf.download(i, start = '2020-01-01', end = '2020-12-31')
        data = rel_std(df)
        arr.append("{:.2f}".format(data))
    print("Program that calculates relative standard deviation for eight Dow Jones companies.")
    # created two dictionaries
    stock = {"BA":arr[0], "KO":arr[1], "XOM":arr[2], "GE":arr[3], "JPM":arr[4], "NKE":arr[5], "PFE":arr[6], "VZ":arr[7]}
    tickers = {"BA":"Boeing", "KO":"Coca-Cola","XOM":"Exxon Mobil", "GE":"General Electric", "JPM":"JPMorgan Chase", "NKE":"Nike", "PFE":"Pfizer", "VZ":"Verizon"}
    # created table that looks similar to sample output using formatting functions
    print("Companies \t\tRelative Standard Deviation")
    print("--------------------------------------------")
    for key in tickers:
        print(tickers[key].ljust(20), stock[key].rjust(10))


main()