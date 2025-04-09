#!/usr/bin/env python  
# encoding: utf-8

# @version: v1.0
# @author: Kandy.Ye
# @contact: Kandy.Ye@outlook.com
# @file: triangle_arbitrage.py
# @time: 星期一 2025/2/17 8:58

from pprint import pprint
from time import sleep
import ccxt


class TriangleArbitrage(object):
    def __init__(self, exchange: str, principal: int = 10000, profit_margin: float = 0.05):
        self.exchange = exchange
        self.profit_info = []
        self.principal = principal  # 本金
        self.profit = profit_margin * principal # 预期利润

    def main(self):
        exchange_class = getattr(ccxt, self.exchange)
        client = exchange_class()
        markets = client.load_markets()

        # 筛选出所有支持USDT和BTC计价的币对
        symbols = []
        for market in markets:
            if markets[market]['active'] and markets[market]['spot'] and 'BTC' == markets[market]['quote']:
                if markets[market]['base'] + '/USDT' in markets:
                    symbols.append(markets[market]['base'])

        for i in range(len(symbols)):
            print('==========  ' + symbols[i] + '  =========')
            try:
                # 获取USDT和BTC的价格
                usdt_ticker = client.fetch_ticker(symbols[i] + '/USDT')
                base_price = usdt_ticker['last']
                # print('USDT price: ' + str(base_price))
                btc_ticker = client.fetch_ticker('BTC/USDT')
                btc_price = btc_ticker['last']
                # print('BTC price: ' + str(btc_price))
                # 获取币对的价格
                symbol_ticker = client.fetch_ticker(symbols[i] + '/BTC')
                symbol_price = symbol_ticker['last']
                # print('symbol/BTC price: ' + str(symbol_price))
                # 计算套利收益
                profit = btc_price * symbol_price * self.principal / base_price - self.principal
                print(symbols[i] + ' => btc => usdt: ' + str(profit))
                if profit > self.profit:
                    self.profit_info.append({
                        'symbol': symbols[i],
                        'profit': profit,
                        'trace':  'USDT =>' + symbols[i] + ' => BTC => USDT'
                    })

                # 计算套利收益
                profit = base_price * self.principal / (btc_price * symbol_price) - self.principal
                print('btc => ' + symbols[i] + ' => usdt: ' + str(profit))
                if profit > self.profit:
                    self.profit_info.append({
                        'symbol': symbols[i],
                        'profit': profit,
                        'trace': 'USDT => BTC => ' + symbols[i] + ' => USDT'
                    })

                if i % 5 == 0:
                    sleep(2)
            except Exception as e:
                print(e)
                sleep(10)
                continue

        pprint(self.profit_info)
        client.close()

        return {
            'symbols': self.profit_info,
            'result': "success"
        }