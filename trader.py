#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import time # pause loop

# -- personal lib --
import request_candles as rc
import request_order as ro
import R_ts_functions as r
import ts_analysis_functions as ts

from IPython.display import clear_output # clear output

import sys # clear output


# In[ ]:


# def trade0(rec):
    
#     counter = 0
    
#     while True:
#         counter = counter + 1
        
#         Y = ts.get_ts(40)

#         # 주문 조건 로직
#         # 매수
#         if (req.get_coin_balance() < 0): # 보유 코인이 없다면
#             if counter%2 == 0:
#                 print('[{}] ready..'.format(counter), flush=True)
#             else:
#                 print('[{}] ready...'.format(counter), flush=True)

#             if () : # 매수조건
#                 print('buy!')
#                 order = ro.ord_bid_price(ro.get_balance() * 0.99) # 매수
#         else: # 코인 잔고가 있다면
#             price = req.get_curret_price()
#             coast = req.get_buy_price()
#             if counter%2 == 0:
#                 print('[{}] profit : {} hold... '.format(counter, (price-coast)/coast), flush=True)
#             else:
#                 print('[{}] profit : {} hold.. '.format(counter, (price-coast)/coast), flush=True)
                
#             if ( price < coast * 0.9995): # 매수 가격보다 내려간다면
#                 order = req.ord_ask_market() # 매도
#                 rec.append(order)
#                 print('sell')
#                 print(order)
#             elif (): # 매도 조건
#                 order = req.ord_ask_market() # 매도
#                 rec.append(order)
#                 print('profit!')
#                 print(order)
    
#         ts.show_plot_trade()
#         time.sleep(1)
#         clear_output(wait = True)
        
#         ts.show_plot_trade()


# In[2]:


def trade2(rec, option):
    """
    5분 이동평균선이 긴 20분 이동평균선을 역전할때 매수
    목표 수익률 0.1%
    """
    print(ro.get_balance())

    while True:
        
        Y = ts.get_ts(40, option = option)

        ma_5 = ts.get_ma(Y, candles = 5)
        ma_20 = ts.get_ma(Y, candles = 20)
        
        a_ = ma_5[len(ma_5)-1] # a'
        a = ma_5[len(ma_5)-2] # a
        b_ = ma_20[len(ma_20)-1] # b'
        b = ma_20[len(ma_20)-2] # b

        slope = r.diff(ma_5)

        # 주문 조건 로직
        # 매수
        if (ro.get_coin_balance() < 0): # 보유 코인이 없다면
            if b > a and b_ < a_ : # ma_1이 ma_2를 넘으면
                print('buy!')
                order = ro.ord_bid_price(ro.get_balance() * 0.99) # 매수
                rec.append(order)
        else: # 코인 잔고가 있다면
            price = ts.get_curret_price()
            coast = ro.get_buy_price()
                
            if ( price < coast * 0.9989): # 매수 가격보다 내려간다면
                order = ro.ord_ask_market() # 매도
                rec.append(order)
                print('loss...')
                print('profit : {}'.format((price-coast)/coast))
                print(order)
            elif( price > coast * 1.00051 ): # 목표 수익률
                order = ro.ord_ask_market() # 매도
                rec.append(order)
                print('profit!')
                print('profit : {}'.format((price-coast)/coast))
                print(order)
                
                
        time.sleep(1)


# In[14]:


# Y = ts.get_ts(40, option = 4)

# ma_20 = ts.get_ma(Y, candles = 20)

# slope = r.diff(ma_20)

# slope[-1:] > 0 


# In[27]:


def trade3(rec, option):
    """
    20일 이동평균선이 상승중일때 매수
    목표 수익률 1%
    """
    counter = 0
    
    while True:
        counter = counter + 1
        
        ma_20 = ts.get_ma(Y, candles = 20)
        
        Y = ts.get_ts(40)

        # 주문 조건 로직
        # 매수
        if (req.get_coin_balance() < 0): # 보유 코인이 없다면
            #log
            if counter%2 == 0:
                print('[{}] ready..'.format(counter), flush=True)
            else:
                print('[{}] ready...'.format(counter), flush=True)

            if (ma) : # 매수조건
                print('buy!')
                order = ro.ord_bid_price(ro.get_balance() * 0.99) # 매수
        else: # 코인 잔고가 있다면
            price = req.get_curret_price()
            coast = req.get_buy_price()
            
            # log
            if counter%2 == 0:
                print('[{}] profit : {} hold... '.format(counter, (price-coast)/coast), flush=True)
            else:
                print('[{}] profit : {} hold.. '.format(counter, (price-coast)/coast), flush=True)
                
            if ( price < coast * 0.981): # 매수 가격보다 내려간다면
                order = req.ord_ask_market() # 매도
                rec.append(order)
                print('sell')
                print(order)
            elif ( price > coast * 1.009): # 매도 조건
                order = req.ord_ask_market() # 매도
                rec.append(order)
                print('profit!')
                print(order)
    
        ts.show_plot_trade()
        time.sleep(1)
        clear_output(wait = True)
        
        ts.show_plot_trade()


# In[3]:


# rec = []

# trade2(rec, option = 1)


# In[5]:


# !jupyter nbconvert --to script trader.ipynb

