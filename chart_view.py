import plotille
import pandas as pd
import candle_store
import pandas as pd
import candle_store

def drawMarket(fig, data):
    # fig.plot(
    #     data['reg'],
    #     data['open'],
    #     lc=4,
    #     label='First line',
    # )
    # fig.plot(
    #     data['reg'],
    #     data['close'],
    #     lc=4,
    #     label='First line'
    # )
    fig.scatter(
        data['reg'],
        data['high'],
        lc=5,
    )
    fig.scatter(
        data['reg'],
        data['low'],
        lc=6
    )

def drawMA(fig, window_size, lc):
    data = candle_store.getMA(window_size)
    fig.plot(
        data['reg'],
        data['SMA'],
        lc=lc
    )

def showCandlePlot():
    plotData = candle_store.plotData()

    fig = plotille.Figure()
    fig.width = 90
    fig.height = 30
    fig.color_mode = 'byte'
    fig.set_x_limits(min_=0, max_=155)
    
    drawMarket(fig, plotData)
    drawMA(fig, window_size=15, lc=1)
    drawMA(fig, window_size=50, lc=2)

    print(fig.show())

showCandlePlot()
