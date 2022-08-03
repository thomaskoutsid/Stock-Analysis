'''
Thomas Koutsidis
7/10/22
Question 4
Program that finds the longest period a stock was up in 2020.
'''

import pandas as pd
import yfinance as yf


def max_up(stock):
    days_above_before = 0
    max_period = 0
    start_period = 0
    for i in range(1, len(stock)):
            if stock["Close"][i] > stock["Close"][i - 1]:
                days_above_before += 1
            else:
                if days_above_before > max_period:
                    max_period = days_above_before
                    start_period = i - max_period
                days_above_before = 0
                
    start_date = stock["Close"].index[start_period]
    value1 = stock["Close"][start_period]
    date1 = start_date.date()
    end_date = stock["Close"].index[start_period + max_period - 1]
    value2 = stock["Close"][start_period + max_period - 1]
    date2 = end_date.date()
   

    return max_period, date1, date2, value1, value2

    
def main():
    print("Program that finds the longest period a stock was up in 2020.")
    stock = input("Please enter the stock symbol: ")
    df = yf.download(stock, start = '2020-01-01', end = '2020-12-31')
    
    length, start, end, value1, value2 = max_up(df)
    print("The longest up period for the stock symbol", stock.upper(),":")
    print("Length in days:", length)
    print("Period started on:", start)
    print("Close stock value at start:", "{:.2f}".format(value1))
    print("Period ended on:", end)
    print("Close stock value at end:", "{:.2f}".format(value2))
    
    
main()