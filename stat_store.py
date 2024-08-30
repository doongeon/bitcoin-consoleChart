import upbit

def getRateOfReturn():
    buyPrice = upbit.getBuyPrice()
    currentPrice = getCurrentPrice()
    return round((currentPrice / buyPrice * 100) - 100, 2)

def getCurrentPrice():
    return upbit.getCurrentPrice()[0]['trade_price']

def getProfit():
    return round(upbit.getCoinBalance() * (getCurrentPrice() - upbit.getBuyPrice()))