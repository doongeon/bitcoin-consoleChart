import candle
import pandas as pd

def dataFrame():
    candles = candle.getCandles()
    result = pd.DataFrame(candles[::-1])
    result["time"] = pd.to_datetime(result["candle_date_time_kst"]).dt.strftime('%H:%M')
    return result

def plotData():
    df = dataFrame()
    return {
        'reg': df.index,
        'time': df['time'],
        'open': df['opening_price'],
        'close': df['trade_price'],
        'high': df['high_price'],
        'low': df['low_price']
    }


def getMA(window_size):
    # 이동 평균선 계산 (SMA)
    df = dataFrame()
    df['SMA'] = df['trade_price'].rolling(window=window_size).mean()
    df = df.dropna(subset=['SMA'])
    
    return {
        'reg': df.index,
        'SMA': df['SMA']
    }