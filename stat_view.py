import upbit
import stat_store as StatStore

def balance_view():
    print(f'****    cash balance: {upbit.getCashBalance()} WON')
    print(f'****    coin balance: {upbit.getCoinBalance()} BTC')

def returnView():
    print(f'****    getRateOfReturn: {StatStore.getRateOfReturn()} %')
    print(f'****    profit: {StatStore.getProfit()} WON')

def show():
    print("*****************************************************************")
    print("****")
    balance_view()
    returnView()
    print("****")
    print("*****************************************************************")

