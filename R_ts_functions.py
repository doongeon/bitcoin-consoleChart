#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[5]:


# R에서 사용한 함수 구현

############################################################################
# plot
# 입력 : dataframe ( 시계열 )
# 출력 : 시계열 plot
############################################################################

def plot(Y, add_xlim = 0):
    plt.figure(figsize=(14,6))
    
    plt.plot(Y)
    plt.xlim(0, len(Y)+add_xlim)
    
    plt.title('time series', fontdict={'fontsize' : 30})
    plt.ylabel('Y', fontdict={'fontsize' : 20})
    plt.xlabel('lags', fontdict={'fontsize' : 20})

    plt.show()

    
############################################################################
# diff
# 입력 : [ dataframe, (int)n ]
#        dataframe ( 차분할 시계열 )
#        n ( 차분 계수 )
# 출력 : 차분된 시계열
############################################################################
    
def diff(Y, n = 1):
    return Y - Y.shift(n)




############################################################################
# adf test
# h0 시계열은 단위근을 포함한다 ( not stationary )
############################################################################

from statsmodels.tsa.stattools import adfuller

def adf_test(Y):
    temp = Y.dropna()
    result = adfuller(temp)
    print('ADF Statistic: %f' % result[0])
    print('p-value: %f' % result[1])
    print('Critical Values:')
    for key, value in result[4].items():
        print('\t%s: %.3f' % (key, value))
        
        
        
############################################################################
# acf plot
# 입력 : (time series, lag)
#        time series ( 데이터프레임 형식 )
#        lag ( int 양의 정수 )
# 출력 : acf plot을 반환
############################################################################

import statsmodels.api as sm

def acf(Y, lags = 20):
    if (len(Y) < 20):
        lags = len(Y)-1
    sm.graphics.tsa.plot_acf(Y, lags = lags)


# In[6]:


# !jupyter nbconvert --to script R_ts_functions.ipynb

