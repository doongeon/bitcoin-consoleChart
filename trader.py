#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import time # pause loop

# -- personal lib --
import request_chart as chart
import request_order as req
import R_ts_functions as r
import ts_analysis as ts


# In[2]:


# In[7]:


# def trade1(rec):
    
#     Y = ts.get_ts(40)

#     ma_5 = ts.get_ma(Y, days = 5)
#     ma_20 = ts.get_ma(Y, days = 20)

#     a_ = ma_5[len(ma_5)-1] # a'
#     a = ma_5[len(ma_5)-2] # a
#     b_ = ma_20[len(ma_20)-1] # b'
#     b = ma_20[len(ma_20)-2] # b

#     slope = r.diff(ma_5)

#     # 매초 갱신

#     # 주문 조건 로직
#     # 매수
#     if (req.get_coin_balance() < 0): # 보유 코인이 없다면
#         print('ready...')
#         if b > a and b_ < a_ : # ma_1이 ma_2를 넘으면
#             print('buy!', flush=True)
#             order = req.ord_bid_price(req.get_balance() * 0.99) # 매수
#             rec.append(order)
#     else: # 코인 잔고가 있다면
#         price = chart.get_curret_price()
#         coast = req.get_buy_price()
#         print('hold... profit : {}'.format((price-coast)/coast), flush=True)
#         if ( price < coast * 0.9995): # 매수 가격보다 내려간다면
#             order = req.ord_ask_market() # 매도
#             rec.append(order)
#             print('sell', flush=True)
#             print(order)
#         elif( slope.to_list()[-1] < -6000 ): # gradient of ma_5 goes under 0
#             order = req.ord_ask_market() # 매도
#             rec.append(order)
#             print('profit!', flush=True)
#             print(order)


# In[13]:


from IPython.display import clear_output # clear output

def trade2(rec):
    
    counter = 0
    
    while True:
        counter = counter + 1
        
        Y = ts.get_ts(40)

        ma_5 = ts.get_ma(Y, days = 5)
        ma_20 = ts.get_ma(Y, days = 20)

        a_ = ma_5[len(ma_5)-1] # a'
        a = ma_5[len(ma_5)-2] # a
        b_ = ma_20[len(ma_20)-1] # b'
        b = ma_20[len(ma_20)-2] # b

        slope = r.diff(ma_5)

        # 주문 조건 로직
        # 매수
        if (req.get_coin_balance() < 0): # 보유 코인이 없다면
            if counter%2 == 0:
                print('[{}] ready..'.format(counter), flush=True)
            else:
                print('[{}] ready...'.format(counter), flush=True)

            if b > a and b_ < a_ : # ma_1이 ma_2를 넘으면
                print('buy!')
                order = req.ord_bid_price(req.get_balance() * 0.99) # 매수
                rec.append(order)
        else: # 코인 잔고가 있다면
            price = req.get_curret_price()
            coast = req.get_buy_price()
            if counter%2 == 0:
                print('[{}] profit : {} hold... '.format(counter, (price-coast)/coast), flush=True)
            else:
                print('[{}] profit : {} hold.. '.format(counter, (price-coast)/coast), flush=True)
                
            if ( price < coast * 0.9995): # 매수 가격보다 내려간다면
                order = req.ord_ask_market() # 매도
                rec.append(order)
                print('sell')
                print(order)
            elif( slope.to_list()[-1] < -6000 ): # gradient of ma_5 goes under 0
                order = req.ord_ask_market() # 매도
                rec.append(order)
                print('profit!')
                print(order)
                
        ts.show_plot_trade()
        time.sleep(30)
        clear_output(wait = True)
        
        ts.show_plot_trade()


# In[11]:


# !jupyter nbconvert --to script trader.ipynb

