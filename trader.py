import upbit
import candle_store as CandleStore
import stat_store as StatStore

logs = [f"start cash balance: {upbit.getCashBalance()}"]

def isCall():
    ma15 = CandleStore.getMA(15)
    ma50 = CandleStore.getMA(50)
    isTrendGoHigh = ma50['SMA'].tolist()[-1] < ma15['SMA'].tolist()[-1]
    isMaRising = ma15['SMA'].tolist()[-4] < ma15['SMA'].tolist()[-1]
    return isTrendGoHigh & isMaRising

def isPut():
    ma15 = CandleStore.getMA(15)
    ma50 = CandleStore.getMA(50)
    isTrendGoLow = ma50['SMA'].tolist()[-1] > ma15['SMA'].tolist()[-1]
    isMaFalling = ma15['SMA'].tolist()[-4] > ma15['SMA'].tolist()[-1]
    return isTrendGoLow or isMaFalling

def run():
    if upbit.getCoinBalance() == 0:
        if isCall():
            upbit.buyCoin()
    else:
        if isPut():
            logs.append(f"trade result: {StatStore.getProfit()}")
            upbit.sellCoin()

    for log in logs:
        print(log)