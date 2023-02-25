#!/usr/bin/env python
# coding: utf-8

# In[13]:


# !pip install requests
# !pip install nbconvert


# In[14]:


import requests


# In[15]:


# 일단은 비트코인 시장만을 목표로

############################################################################
# 분캔들
# 입력 : 캔들 개수 (최대 200)
# 출력 : 캔들 정보에 해당하는 json list 
#        ex) [ 0 ] ( 현재 ) ~ [ 입력-1 ] ( 과거 )
############################################################################

def candle_mins(mins, count):
    url = "https://api.upbit.com/v1/candles/minutes/{}?market=KRW-BTC&count={}".format(mins, count)
    
    headers = {"accept": "application/json"}

    response = requests.get(url, headers=headers)

    return response.json()

def candle_min_01(count):
    return candle_mins(1, count)

def candle_min_15(count):
    return candle_mins(15, count)

def candle_min_30(count):
    return candle_mins(30, count)


############################################################################
# 현재가 정보
# 입력 : .
# 출력 : 현재 가격정보에 해당하는 json
############################################################################

def current_price():
    url = "https://api.upbit.com/v1/ticker/?markets=KRW-BTC"

    headers = {"accept": "application/json"}

    response = requests.get(url, headers=headers)

    return response.json()

def get_curret_price():
    return current_price()[0]['trade_price']


# In[ ]:


get_ipython().system('jupyter nbconvert --to script request_chart.ipynb')

