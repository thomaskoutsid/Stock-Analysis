'''
Thomas Koutsidis
7/9/22
Question 3
Program that calculates sample correlation between Boeing and Coca Cola closing stock values in 2020
'''


import pandas as pd
import yfinance as yf


def correl(stock1, stock2):
    sum1 = 0
    m, n = stock1.shape
    for x in stock1["Close"]:
        sum1 += x
    x_hat1 = sum1 / m
    
    sum_sq1 = 0
    for x in stock1["Close"]:
        sum_sq1 += (x - x_hat1)**2
    
    var1 = sum_sq1 / (m - 1)
    std1 = var1 ** (1/2)   
    
    sum2 = 0
    m, n = stock2.shape
    for x in stock2["Close"]:
        sum2 += x
    x_hat2 = sum2 / m
    
    sum_sq2 = 0
    for x in stock2["Close"]:
        sum_sq2 += (x - x_hat2)**2
    
    var2 = sum_sq2 / (m - 1)
    std2 = var2 ** (1/2)
    
    sum_cov1 = 0
    for i in stock1["Close"]:
        sum_cov1 += (i - x_hat1)

    sum_cov2 = 0
    for i in stock2["Close"]:
        sum_cov2 += (i - x_hat2)
        
    cov = (sum_cov1 * sum_cov2) / (m - 1)
    
    cor = cov / (std1 * std2)
    
    print("Program calculates sample correlation between Boeing and Coca Cola closing stock values in 2020.\n")
    print("Average Boeing stock value:", "{:.2f}".format(x_hat1))
    print("Std deviation of Boeing stock:", "{:.2f}".format(std1))
    print("\nAverage Coke stock value:", "{:.2f}".format(x_hat2))
    print("Std deviation of Coke stock:", "{:.2f}".format(std2))
    print("\nCov =", "{:.2f}".format(cov))
    
    return cor


def main():
    symbols = ['ba', 'ko']
    arr = []
    for i in symbols:
        df = yf.download(i, start = '2020-01-01', end = '2020-12-31')
        arr.append(df)
    ba = arr[0]
    ko = arr[1]
    
    cor = correl(ba, ko)
    
    print("\nCorrelation between BA and KO:", "{:.2f}".format(cor))
    

main()
    
    
    
