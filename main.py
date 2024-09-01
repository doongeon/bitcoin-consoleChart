import chart_view as chartView
import stat_view as StatView
import trader
import time
import os

while 1:
    os.system('clear')

    trader.run()
    StatView.show()
    chartView.showCandlePlot()

    time.sleep(30)
