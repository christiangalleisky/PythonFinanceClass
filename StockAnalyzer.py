import quandl
import numpy as np
import pandas as pd
import matplotlib
import math
import random
import statsmodels
import pandas_datareader
from pandas_datareader import data as wb
import matplotlib.pyplot as plt


num =  np.random.randint(0, 7, (4, 6))
print(num)
x = np.random.random(5)
print(x)
ser = pd.Series(x, name = 'Column 15')
print(ser)



tickers= ["MSFT", "INTC", "GOOG", 'XOM', 'CVX', 'CLR']
opens = pd.DataFrame()
highs = pd.DataFrame()
lows = pd.DataFrame()
close = pd.DataFrame()
volume = pd.DataFrame()
for t in tickers:
    opens[t] = wb.DataReader(t, data_source='yahoo', start='2008-1-1')['Open']
    highs[t] = wb.DataReader(t, data_source='yahoo', start='2008-1-1')['High']
    lows[t] = wb.DataReader(t, data_source='yahoo', start='2008-1-1')['Low']
    close[t] = wb.DataReader(t, data_source='yahoo', start='2008-1-1')['Close']
    volume[t] = wb.DataReader(t, data_source='yahoo', start='2008-1-1')['Volume']
print("opens values:")
print(opens)
print("highs values:")
print(highs)
print("lows values:")
print(lows)
print("close values:")
print(close)
print("volume values:")
print(volume)
print(" ")
print(" ")
print(" ")

'''
mydata = quandl.get_table('ZACKS/FC', ticker='AAPL')
print(mydata)
mydata.to_csv(destination directory.csv)
someFile = pd.read_csv(directory.csv)
someFile.to_excel(direcotry.xlsx)
lastFile = pd.read_excel(directory.xlsx)
'''

