# btc-cent-forecast-01

Entry for make.fun bounty [btc-cent-forecast-01](https://make.fun/bounty/btc-cent-forecast-01).

`main.py` (Python 3, stdlib only, offline) reads a case file of 72h of 1-minute BTC/USDC closes and forecasts the close 240 minutes after the checkpoint. The forecast is a weighted blend: 40% last close + 30% mean of last 120 minutes + 30% mean of last 360 minutes, clamped to the scorer's price bounds.
