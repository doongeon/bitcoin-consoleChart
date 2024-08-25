import requests

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
# 분캔들
# 입력 : 캔들 개수 (최대 200)
# 출력 : 캔들 정보에 해당하는 json list 
#        ex) [ 0 ] ( 현재 ) ~ [ 입력-1 ] ( 과거 )
############################################################################

def candle_days(count):
    url = "https://api.upbit.com/v1/candles/days?market=KRW-BTC&count={}".format(count)

    headers = {"accept": "application/json"}

    response = requests.get(url, headers=headers)

    return response.json()
