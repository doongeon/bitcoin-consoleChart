import pandas as pd
import numpy as np
import termplotlib as tpl
import request_candles as rc
import requests


def req_candles(count, option):
    """
    req_candles
    input : (int) count, (int) option
    output : (dataframe) candles
    description : 
        count {
            length of dataframe
        }
        
        option {
            1 (1 min)
            2 (15 mins)
            3 (30 mins)
            4 (1 day)
        }
    """
    
    try:
        if (option == 1):
            candles = rc.candle_min_01(count)
        elif (option == 2):
            candles = rc.candle_min_15(count)
        elif (option == 3):
            candles = rc.candle_min_30(count)
        elif (option == 4):
            candles = rc.candle_days(count)
        else:
            print('wrong option...')
            return -1
        
    except Exception as ex:
        print('에러가 발생 했습니다', ex)
        return -1

    candles = pd.DataFrame(candles)
    candles = candles[::-1].reset_index(drop=1)
    
    return candles







def get_open_price(count, option):
    """
    get price series
    input : (int) count
    output : (series) price list
    description :
    count {
        length of dataframe
    }
    
    option {
        1 (1 min)
        2 (15 mins)
        3 (30 mins)
        4 (1 day)
    }
    """
    return req_candles(count, option)[['opening_price']].squeeze()







def get_trade_price(count, option):
    """
    get price series
    input : (int) count
    output : (series) price list
    description : 
        count {
            length of dataframe
        }
        
        option {
            1 (1 min)
            2 (15 mins)
            3 (30 mins)
            4 (1 day)
        }
    """
    return req_candles(count, option = 1)[['trade_price']].squeeze()






def current_price():
    """
    현재 시장가 json 들고오기
    입력 : .
    출력 : 현재 시장가 json
    """
    url = "https://api.upbit.com/v1/ticker/?markets=KRW-BTC"

    headers = {"accept": "application/json"}

    response = requests.get(url, headers=headers)

    return response.json()








def get_curret_price():
    """
    현재 시장가 들고오기
    입력 : .
    출력 : (float) 현재 시장가
    """
    return float(current_price()[0]['trade_price'])

    
    
    
    
    


def get_ma(Y, candles = 5):
    """
    평균이동선
    input : ( series, days )
    output : 지난 5일간 평균 가격 dataframe
    """    
    temp = (Y.cumsum() - Y.cumsum().shift(candles)) / candles
    return temp








def get_ts(count, option):
    """
    get_ts
    input : (int) count
    output : (series) time series
    description : 
    count {
        length of dataframe
    }
    option {
        1 (1 min)
        2 (15 mins)
        3 (30 mins)
        4 (1 day)
    }
    """
    temp = get_open_price(count, option)
    
    cur_price = get_curret_price()
    cur_price = pd.Series(float(cur_price))

    temp = pd.concat(
        [temp, cur_price],
        ignore_index=True
    )

    return temp








def show_plot_trade(option, lags = 50):
    """
    ma가 포함된 시세 그래프
    input : (int) lags
    output : .
    description : ma가 포함된 시세 그래프를 보여준다
    """
    Y = get_ts(lags, option)

    ma1 = get_ma(Y, candles = 5)
    ma2 = get_ma(Y, candles = 20)

    fig = tpl.figure()

    fig.plot(Y, label='price')
    fig.plot(ma1, label='ma_5')
    fig.plot(ma2, label='ma_20')

    fig.xlim(20, lags+1)

    if option == 1:
        candle_type = '1min'
    elif option == 2:
        candle_type = '15mins'
    elif option == 3:
        candle_type = '30mins'
    elif option == 4:
        candle_type = 'day'
    
    fig.title('KRW-BTC ({})'.format(candle_type))
    fig.show()
    
    
    
    

    

def show_plot_LowHigh(option, lags = 30):
    """
    시세 그래프
    input : .
    output : 시세 그래프 ( 최고가, 시작가, 최저가 )
    """
    candles = req_candles(lags, option)

    fig = tpl.figure()

    fig.plot(candles['opening_price'], label='open')
    fig.plot(candles['low_price'], label='low')
    fig.plot(candles['high_price'], label='high')

    if option == 1:
        candle_type = '1min'
    elif option == 2:
        candle_type = '15mins'
    elif option == 3:
        candle_type = '30mins'
    elif option == 4:
        candle_type = 'day'

    fig.title('KRW-BTC ({})'.format(candle_type))
    fig.show()
