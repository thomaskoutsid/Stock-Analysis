'''
Thomas Koutsidis
7/8/22
Question 1
Program that calculates IBM stock data statistics for the year 2020.
'''

import pandas as pd
import yfinance as yf

def main():
    
    # download IBM stock for year 2020
    df = yf.download('ibm', start = '2020-01-01', end = '2020-12-31')
    m, n = df.shape
    print("Program that calculates IBM stock data statistics for the year 2020.")
    print("There are", m, "rows of stock data\n")    
    
    sum = 0
    for x in df["Close"]:
        sum += x
    x_hat = sum / m
    print("IBM 2020 average stock value:", "{:.2f}".format(x_hat))
    
    # calculated and printed variance
    sum_sq = 0
    for x in df["Close"]:
        sum_sq += (x - x_hat)**2
    var = sum_sq / (m - 1)
    print("IBM stock variance:", "{:.2f}".format(var))
    
    # calculated and printed standard deviation
    std = var ** (1/2)
    print("IBM stock standard deviation:", "{:.2f}\n".format(std))
    
    # found and printed max and min closing stock values and respective dates
    max = df["Close"].max()
    max_date = df["Close"].idxmax()
    print("The max stock value", "{:.2f}".format(max), "was on", max_date.date())
    min = df["Close"].min()
    min_date = df["Close"].idxmin()
    print("The min stock value", "{:.2f}".format(min), "was on", min_date.date())
    
    
main()