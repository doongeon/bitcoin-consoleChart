#!/usr/bin/env python
# coding: utf-8

# In[4]:


# !pip install pyjwt
import jwt
import hashlib
import requests
import uuid
from urllib.parse import urlencode, unquote
import importlib
import upbit_keys as keys


# In[5]:


server_url = 'https://api.upbit.com'

############################################################################
# make your upbit key file(.py) on same directory
#
# ex) upbit_keys.py
# access_key = ' -* your access key here *-'
# secret_key = ' -* your secret key here *-'
#
############################################################################

############################################################################
# 업비트 자산조회
# 입력 : 업비트 access key, secret key
# 출력 : 나의 자산내용에 해당하는 json
############################################################################

def asset_check(server_url = server_url):
    payload = {
        'access_key': keys.access_key,
        'nonce': str(uuid.uuid4()),
    }

    jwt_token = jwt.encode(payload, keys.secret_key)
    authorization = 'Bearer {}'.format(jwt_token)
    headers = {
      'Authorization': authorization,
    }

    res = requests.get(server_url + '/v1/accounts', headers=headers)
    return res.json()


############################################################################
# 현금계좌 잔액 조회
# 입력 : .
# 출력 : (float) balance
############################################################################

def get_balance():
    assets = asset_check()
    for i, asset in enumerate(assets):
        if(asset['currency'] == 'KRW'):
            return float(asset['balance'])

        
        
############################################################################
# 비트코인 조회
# 입력 : .
# 출력 : (float) volume
############################################################################

def get_coin_balance():
    assets = asset_check()
    for i, asset in enumerate(assets):
        if(asset['currency'] == 'BTC'):
            return float(asset['balance'])
        elif (i == len(assets)-1):
            print('COIN_BALANCE_EMPTY')


        
############################################################################
# 비트코인 구매가격 조회
# 입력 : .
# 출력 : (float) avg_buy_price
############################################################################

def get_buy_price():
    assets = asset_check()
    for i, asset in enumerate(assets):
        if(asset['currency'] == 'BTC'):
            return float(asset['avg_buy_price'])
        elif (i == len(assets)-1):
            print('COIN_BALANCE_EMPTY')

        
############################################################################
# 주문 가능정보 조회
# 입력 : (str) 코인 티커
#        ex) 'BTC'
# 출력 : 입력한 코인 시장 정보 json
############################################################################

def market_price(market, server_url = server_url):
    params = {
      'market': 'KRW-' + market
    }
    query_string = unquote(urlencode(params, doseq=True)).encode("utf-8")

    m = hashlib.sha512()
    m.update(query_string)
    query_hash = m.hexdigest()

    payload = {
        'access_key': keys.access_key,
        'nonce': str(uuid.uuid4()),
        'query_hash': query_hash,
        'query_hash_alg': 'SHA512',
    }

    jwt_token = jwt.encode(payload, keys.secret_key)
    authorization = 'Bearer {}'.format(jwt_token)
    headers = {
      'Authorization': authorization,
    }

    res = requests.get(server_url + '/v1/orders/chance', params=params, headers=headers)
    return res.json()



############################################################################
# 개별 주문 조회
# 입력 : 주문 uuid
#        ex) '00000000-0000-0000-0000-000000000000'
# 출력 : 입력한 주문에 대한 내용 json
############################################################################

def order_check(order_id, server_url = server_url):
    params = {
      'uuid': order_id
    }
    query_string = unquote(urlencode(params, doseq=True)).encode("utf-8")

    m = hashlib.sha512()
    m.update(query_string)
    query_hash = m.hexdigest()

    payload = {
        'access_key': keys.access_key,
        'nonce': str(uuid.uuid4()),
        'query_hash': query_hash,
        'query_hash_alg': 'SHA512',
    }

    jwt_token = jwt.encode(payload, keys.secret_key)
    authorization = 'Bearer {}'.format(jwt_token)
    headers = {
      'Authorization': authorization,
    }

    res = requests.get(server_url + '/v1/order', params=params, headers=headers)
    return res.json()



############################################################################
# 주문 취소 접수
# 미완
#
############################################################################

def cancel_order(server_url = server_url):
    params = {
      'uuid': '00000000-0000-0000-0000-000000000000'
    }
    query_string = unquote(urlencode(params, doseq=True)).encode("utf-8")

    m = hashlib.sha512()
    m.update(query_string)
    query_hash = m.hexdigest()

    payload = {
        'access_key': keys.access_key,
        'nonce': str(uuid.uuid4()),
        'query_hash': query_hash,
        'query_hash_alg': 'SHA512',
    }

    jwt_token = jwt.encode(payload, keys.secret_key)
    authorization = 'Bearer {}'.format(jwt_token)
    headers = {
      'Authorization': authorization,
    }

    res = requests.delete(server_url + '/v1/order', params=params, headers=headers)
    return res.json()



############################################################################
# 업비트 주문하기
# 입력 : 
# 출력 : 매도, 매수 주문내용에 해당하는 json
############################################################################

def coin_order(side_option, price = 'NULL', volume = 'NULL', server_url = server_url):
    params = {
      'market': 'KRW-BTC',
    }
    
    # [side_option] ( 0 : 매수 , 1 : 매도 )
    if side_option == 0: # 매수
        params['side'] = 'bid'
        params['ord_type'] = 'price'
        params['price'] = price
    elif side_option == 1: # 매도
        params['side'] = 'ask'
        params['ord_type'] = 'market'
        params['volume'] = volume
    else:
        print('error form function "coin_order" wrong input in parameter "side_option"')
        return -1;
        
    query_string = unquote(urlencode(params, doseq=True)).encode("utf-8")

    m = hashlib.sha512()
    m.update(query_string)
    query_hash = m.hexdigest()

    payload = {
        'access_key': keys.access_key,
        'nonce': str(uuid.uuid4()),
        'query_hash': query_hash,
        'query_hash_alg': 'SHA512',
    }

    jwt_token = jwt.encode(payload, keys.secret_key)
    authorization = 'Bearer {}'.format(jwt_token)
    headers = {
      'Authorization': authorization,
    }

    res = requests.post(server_url + '/v1/orders', json=params, headers=headers)
    return res.json()



############################################################################
# 시장가 매수
# 입력 : int 매수금액
# 출력 : 실패시 -1 반환
#        성공시 주문내역에 해당하는 json 반환
############################################################################

def ord_bid_price(price):
    if price < (int)(market_price('BTC')['market']['bid']['min_total']):
        print('최소 주문금액은 {} 입니다.'.format(market_price('BTC')['market']['bid']['min_total']))
        return -1;
    else:
        return coin_order(side_option = 0, price = price)

    
    
############################################################################
# 시장가 매도
# 입력 : 매도 물량
#        default : 0 ( 전체 물량 매도 )
# 출력 : 잘못된 입력이 들어왔을떄 -1 반환
#        주문내역에 해당하는 json 반환
############################################################################

def ord_ask_market(volume = 0):
    if(volume == 0): 
        return coin_order(side_option = 1, volume = market_price('BTC')['ask_account']['balance'])
    elif(volume > 0):
        return coin_order(side_option = 1, volume = volume)
    else:
        return -1

    
    
############################################################################
# 전체 주문 조회
# 입력 : .
# 출력 : 전채 주문내역에 해당하는 json list 
#        ex) [0]( 최근 ) ~ [...]( 먼 과거 )
############################################################################

def orderList_check(server_url = server_url):
    params = {
        # [states option] ( 조회할 주문 상태 ) 
      'states[]': ['done', 'cancel']
    }
    query_string = unquote(urlencode(params, doseq=True)).encode("utf-8")

    m = hashlib.sha512()
    m.update(query_string)
    query_hash = m.hexdigest()

    payload = {
        'access_key': keys.access_key,
        'nonce': str(uuid.uuid4()),
        'query_hash': query_hash,
        'query_hash_alg': 'SHA512',
    }

    jwt_token = jwt.encode(payload, keys.secret_key)
    authorization = 'Bearer {}'.format(jwt_token)
    headers = {
      'Authorization': authorization,
    }

    res = requests.get(server_url + '/v1/orders', params=params, headers=headers)
    return res.json()



############################################################################
# 마지막 매수 주문 가져오기
# 입력 : .
# 출력 : 마지막 매수주문에 해당하는 json
############################################################################

def get_last_bid():
    result = ''
    for i, order in enumerate(orderList_check()):
        if (order['side'] == 'bid'):
            result = orderList_check()[i]
            break;
    return result



############################################################################
# 마지막 매도 주문 가져오기
# 입력 : .
# 출력 : 마지막 매도주문에 해당하는 json
############################################################################

def get_last_ask():
    result = ''
    for i, order in enumerate(orderList_check()):
        if (order['side'] == 'ask'):
            result = orderList_check()[i]
            break;
    return result


# In[6]:


get_ipython().system('jupyter nbconvert --to script request_order.ipynb')

