#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import request_order as req
import request_chart as chart
import R_ts_functions as r


# In[2]:


############################################################################
# req_candles
# input : (int) count
# output : (dataframe) candles
# description : .
############################################################################

def req_candles(count):
    candles = chart.candle_min_15(count)
#     candles = chart.candle_min_01(count) # 실험용

    # make as dataframe
    candles = pd.DataFrame(candles)

    # order dataframe as time order
    candles = candles[::-1].reset_index(drop=1)
    
    return candles



############################################################################
# get price series
# input : (int) count
# output : (series) price list
# description : .
############################################################################

def get_open_price(count):
    return req_candles(count)[['opening_price']].squeeze()

def get_trade_price(count):
    return req_candles(count)[['trade_price']].squeeze()

    
    
############################################################################
# 평균이동선
# input : ( series, days )
# output : 지난 5일간 평균 가격 dataframe
############################################################################

def get_ma(Y, days=5):
    temp = (Y.cumsum() - Y.cumsum().shift(days)) / days
    return temp



############################################################################
# get_ts
# input : (int) count
# output : (series) time series
# description : .
############################################################################

def get_ts(count):
    temp = get_open_price(count)
    
    cur_price = req.get_curret_price()
    cur_price = pd.Series(float(cur_price))

    pd.concat(
        [temp, cur_price],
        ignore_index=True
    )

    return temp



############################################################################
# ma가 포함된 시세 그래프
# input : (int) lags
# output : .
# description : ma가 포함된 시세 그래프를 보여준다
############################################################################

def show_plot_trade(lags = 50):
    Y = get_ts(lags)

    ma1 = get_ma(Y, days = 5)
    ma2 = get_ma(Y, days = 20)

    plt.plot(Y)
    plt.plot(ma1)
    plt.plot(ma2)
    plt.xlim(20, lags+1)
    plt.legend(['price', 'ma_5', 'ma_20'])
    plt.xlabel('lag')
    plt.ylabel('price')
    plt.title('KRW-BTC')
    plt.show()
    
    
    
############################################################################
# 시세 그래프
# input : .
# output : 시세 그래프 ( 최고가, 시작가, 최저가 )
############################################################################

def show_plot_LowHigh(lags = 30):
    candles = req_candles(lags)
    
    plt.figure(figsize=(14,6))

    plt.plot(candles[['opening_price', 'low_price', 'high_price']])

    plt.legend(['open', 'low', 'high'])

    plt.title('coin price (30mins)', fontdict={'fontsize' : 30})
    plt.ylabel('price', fontdict={'fontsize' : 20})
    plt.xlabel('lags', fontdict={'fontsize' : 20})

    plt.show()


# In[184]:


# !jupyter nbconvert --to script ts_analysis.ipynb

