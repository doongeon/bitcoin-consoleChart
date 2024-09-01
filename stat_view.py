import upbit
import stat_store as StatStore

def balance_view():
    print(f'****    cash balance: {upbit.getCashBalance()} WON')
    print(f'****    coin balance: {upbit.getCoinBalance()} BTC')

def returnView():
    print(
        f'****    getRateOfReturn: {" - " if upbit.getCoinBalance() == 0 else f"{StatStore.getRateOfReturn()} &"}'
    )
    print(
        f'****    profit: {" - " if upbit.getCoinBalance() == 0 else f"{StatStore.getProfit()} WON"}'
    )

def show():
    print("*****************************************************************")
    print("****")
    balance_view()
    returnView()
    print("****")
    print("*****************************************************************")

