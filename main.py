import requests
import json
import numpy as np
from get_futhers import get_futhers

while True:
    a = get_futhers('ETHUSDT')
    b = get_futhers('BTCUSDT')
    old_price = a[0]
    new_price = a[-1]
    percent = abs((new_price * 100 / old_price)-100)
    cor_coef = abs(np.corrcoef(a,b,dtype=float)[0][1])
    print(cor_coef)
    print(old_price, new_price)
    if percent > 1 and cor_coef < 0.87:
        print("Цена изменилась на больше, чем 1%")
        print(f"Новая цена: {new_price}")






