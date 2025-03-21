import jwt # !pip install pyjwt
import hashlib
import requests
import uuid
from urllib.parse import urlencode, unquote
import upbit_keys as keys

def queryString(params):
    return unquote(urlencode(params, doseq=True)).encode("utf-8")

def getQueryHash(params):
    m = hashlib.sha512()
    m.update(queryString(params))
    return m.hexdigest()

def getRequestHeader(queryHash):
    return {
        'access_key': keys.access_key,
        'nonce': str(uuid.uuid4()),
        'query_hash': queryHash,
        'query_hash_alg': 'SHA512',
    }


# def getAuthorizedHeader(queryHash):
#     return {
#         'Authorization': 'Bearer {}'.format(jwt.encode(getRequestHeader(queryHash), keys.secret_key)),
#     }

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

def getAsset(server_url = server_url):
    payload = {
        'access_key': keys.access_key,
        'nonce': str(uuid.uuid4()),
    }

    headers = {
        'Authorization': 'Bearer {}'.format(jwt.encode(payload, keys.secret_key)),
    }

    res = requests.get(server_url + '/v1/accounts', headers=headers)
    return res.json()


############################################################################
# 현금계좌 잔액 조회
# 입력 : .
# 출력 : (float) balance
############################################################################

def getCashBalance():
    for _, asset in enumerate(getAsset()):
        if(asset['currency'] == 'KRW'):
            return round(float(asset['balance']))

    return 0
############################################################################
# 비트코인 조회
# 입력 : .
# 출력 : (float) volume
#        (int) -1 [코인이 없다면]
############################################################################

def getCoinBalance():
    for _, asset in enumerate(getAsset()):
        if(asset['currency'] == 'BTC'):
            return float(asset['balance'])
        
    return 0

############################################################################
# 비트코인 구매가격 조회
# 입력 : .
# 출력 : (float) avg_buy_price
############################################################################

def getBuyPrice():
    for _, asset in enumerate(getAsset()):
        if(asset['currency'] == 'BTC'):
            return float(asset['avg_buy_price'])
        
    return 0

def getCurrentPrice():
    res = requests.get(
        server_url + '/v1/ticker?markets=KRW-BTC',
        headers = {"accept": "application/json"}
    )
    return res.json()

############################################################################
# 개별 주문 조회
# 입력 : 주문 uuid
#        ex) '00000000-0000-0000-0000-000000000000'
# 출력 : 입력한 주문에 대한 내용 json
############################################################################

# def order_check(order_id, server_url = server_url):
#     params = {
#         'uuid': order_id
#     }
#     res = requests.get(
#         server_url + '/v1/order',
#         params=params,
#         headers=getAuthorizedHeader(queryHash=getQueryHash(params=params))
#     )
#     return res.json()


############################################################################
# 업비트 주문하기
# 입력 : 
# 출력 : 매도, 매수 주문내용에 해당하는 json
############################################################################

# def buyCoin():
#     params = {
#         'market': 'KRW-BTC',
#         'side': 'bid',
#         'ord_type': 'price',
#         'price': f'{getCashBalance() * 0.99}'
#     }

#     res = requests.post(
#         server_url + '/v1/orders',
#         json=params,
#         headers=getAuthorizedHeader(queryHash=getQueryHash(params=params))
#     )

    # return res.json()

# def sellCoin():
#     params = {
#         'market': 'KRW-BTC',
#         'side': 'ask',
#         'ord_type': 'market',
#         'volume': f'{getCoinBalance()}'
#     }

#     res = requests.post(
#         server_url + '/v1/orders',
#         json=params,
#         headers=getAuthorizedHeader(queryHash=getQueryHash(params=params))
#     )
#     return res.json()



def orderCoin(side_option, price = 'NULL', volume = 'NULL', server_url = server_url):
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
        print('error form function "orderCoin" wrong input in parameter "side_option"')
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
# 전체 주문 조회
# 입력 : .
# 출력 : 전채 주문내역에 해당하는 json list 
#        ex) [0]( 최근 ) ~ [...]( 먼 과거 )
############################################################################

# def orderList_check(server_url = server_url):
#     params = {
#         # [states option] ( 조회할 주문 상태 ) 
#         'states[]': ['done', 'cancel']
#     }
#     queryString = unquote(urlencode(params, doseq=True)).encode("utf-8")
#     queryHash = getQueryHash(queryString=queryString)
#     headers = getAuthorizedHeader(queryHash=queryHash)
#     res = requests.get(server_url + '/v1/orders', params=params, headers=headers)
#     return res.json()

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
