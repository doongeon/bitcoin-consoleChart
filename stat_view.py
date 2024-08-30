import upbit

def balance_view():
    print(f'cash balance: {upbit.getCashBalance()} WON')
    print(f'coin balance: {upbit.getCoinBalance()} BTC')

def returnView():
    print(f'getBuyPrice: {upbit.getBuyPrice()}')
    # print(f'return: {} WON')
    # print(f'rate of return: {} %')