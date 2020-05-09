import numpy as np
import pandas as pd
import matplotlib
import math
import random
import statsmodels
import pandas_datareader
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
'''
num =  numpy.random.randint(0, 7, (4, 6))
print(num)

x = numpy.random.random(5)
print(x)

ser = pandas.Series(x, name = 'Column 1')
print(ser)

#PG = wb.DataReader('PG', data_source='yahoo', start ='2010-1-1')
#print(PG)

#PG.info()

tickers= ["MSFT", "INTC", "GOOG"]
new_data = pd.DataFrame()
for t in tickers:
    new_data[t] = wb.DataReader(t, data_source='yahoo', start='2010-1-1')['Close']
#print(new_data)


PG.head()

PG.tail()

PG['simple returns'] = (PG['Close'] / PG['Close'].shift(1)) - 1
print(PG['simple returns'])

PG['simple returns'].plot(figsize = (8, 5))
plt.show()

ave_returns_d = PG['simple returns'].mean()
print(ave_returns_d)
ave_returns_a = PG['simple returns'].mean() *250
print(ave_returns_a)
print(str(round(ave_returns_a, 5) * 100) + '%')

PG['log returns'] = np.log(PG['Close'] / PG['Close'].shift(1))
print PG['log returns']

PG['log returns'].plot(figsize = (8, 5))
plt.show()

ave_log_returns_d = PG['log returns'].mean()
print(ave_log_returns_d)
ave_log_returns_a = PG['log returns'].mean() * 250
print(ave_log_returns_a)
print(str(round(ave_log_returns_a, 5) * 100) + '%')

(new_data / new_data.iloc[0] * 100).plot(figsize = (15, 6))
plt.show()

new_data.plot(figsize = (15, 6))
plt.show()

returns = (new_data / new_data.shift(1)) - 1
weights = [0.25, 0.25, 0.5]
returns_annual = returns.mean() * 250
x = np.dot(returns_annual, weights)
print(x)
portfolio_1 = str(round(x, 5) * 100) + '%'
print("ANNUAL RETURNS:")
print(portfolio_1)
'''
'''
indices_tickers = ['^GSPC', '^IXIC', '^GDAXI']
indices_data = pd.DataFrame()
for t in indices_tickers:
    indices_data[t] = wb.DataReader(t, data_source='yahoo', start='2000-1-1')['Close']
(indices_data / indices_data.iloc[0] * 100).plot(figsize = (15, 6))
plt.show()

indices_data.plot(figsize = (15, 6))
plt.show()

indices_returns = (indices_data / indices_data.shift(1)) - 1
annual_indices_returns = indices_returns.mean() * 250
print(annual_indices_returns)
'''
oil_and_gas_tickers = ['XOM', 'CVX', 'CLR']
web_page_scraped = 'yahoo'
sec_data = pd.DataFrame()
for t in oil_and_gas_tickers:
    sec_data[t] = wb.DataReader(t, web_page_scraped, '2000-1-1')['Close']
sec_returns = np.log(sec_data / sec_data.shift(1))
sec_returns['XOM'].mean() * 250
sec_returns['XOM'].std() * 250 ** 0.5
sec_returns['CVX'].mean() * 250
sec_returns['CVX'].std() * 250 ** 0.5
sec_returns['CLR'].mean() * 250
sec_returns['CLR'].std() * 250 ** 0.5

oAg_mean = sec_returns[['XOM', 'CVX', 'CLR']].mean() * 250
oAg_std_dev = sec_returns[['XOM', 'CVX', 'CLR']].std() * 250 ** 0.5

print(oAg_mean)
print(oAg_std_dev)