#!/usr/bin/env python3
"""btc-cent-forecast-01 entry: weighted blend of recent closes (4h-ahead point forecast)."""
import json, os, glob, statistics

IN = os.environ.get('MAKEFUN_INPUT_DIR', '/input')
OUT = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')

def forecast(prices):
    last = prices[-1]
    m120 = statistics.mean(prices[-120:])
    m360 = statistics.mean(prices[-360:])
    g = 0.4 * last + 0.3 * m120 + 0.3 * m360
    return max(0.00001, min(9999999.99999, round(g, 5)))

os.makedirs(OUT, exist_ok=True)
for path in sorted(glob.glob(os.path.join(IN, '*.in'))):
    case = json.load(open(path))
    cid = case['case']
    prices = case['markets'][0]['prices']
    guess = forecast(prices)
    out = {'forecasts': [{'case': cid, 'price': guess}]}
    with open(os.path.join(OUT, cid + '.out'), 'w') as fh:
        json.dump(out, fh)
