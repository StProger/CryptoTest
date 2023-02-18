import requests
import json
def get_futhers(symbol, interval = '1m'):
    params = {
        'symbol': symbol,
        'interval': interval
    }
    url = 'https://api.binance.com/api/v1/klines'
    data = json.loads(requests.get(url = url, params= params).text)
    info = [float(i[4]) for i in data]
    return info