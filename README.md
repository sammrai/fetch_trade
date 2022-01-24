# this is
a trade logger.

# usage:
docker run --rm sammrai/fetch_trade:latest [-h] --exchanges [EXCHANGES [EXCHANGES ...]] --symbols
                      [SYMBOLS [SYMBOLS ...]] [--out OUT] [--loop LOOP]

or run it in your environment:

python fetch_trade.py [-h] --exchanges [EXCHANGES [EXCHANGES ...]] --symbols
                      [SYMBOLS [SYMBOLS ...]] [--out OUT] [--loop LOOP]

# example:

```
$ docker run --name fetch_trade --restart=always -d -v $(pwd)/data:/data sammrai/fetch_trade:latest --exchanges liquid bitflyer coincheck gmocoin --symbols BTC/JPY ETH/JPY XRP/JPY --out /data

==> bitFlyer_BTC_JPY_20220124.txt <==
BTC/JPY,sell,0.01,3794769.0,2022-01-24T13:40:52.880Z,bitFlyer,1643031652880
BTC/JPY,sell,0.01,3793969.0,2022-01-24T13:40:53.193Z,bitFlyer,1643031653193
BTC/JPY,sell,0.01,3793785.0,2022-01-24T13:40:53.193Z,bitFlyer,1643031653193
BTC/JPY,sell,0.01,3793472.0,2022-01-24T13:40:53.280Z,bitFlyer,1643031653280
BTC/JPY,sell,0.006,3793250.0,2022-01-24T13:40:53.280Z,bitFlyer,1643031653280
BTC/JPY,buy,0.01,3793702.0,2022-01-24T13:40:53.550Z,bitFlyer,1643031653550
BTC/JPY,sell,0.34922503,3791237.0,2022-01-24T13:40:53.767Z,bitFlyer,1643031653767
BTC/JPY,sell,0.01,3791237.0,2022-01-24T13:40:53.800Z,bitFlyer,1643031653800
BTC/JPY,sell,0.04077497,3791237.0,2022-01-24T13:40:53.817Z,bitFlyer,1643031653817
BTC/JPY,sell,0.01,3791201.0,2022-01-24T13:40:53.817Z,bitFlyer,1643031653817
BTC/JPY,sell,0.03922503,3791092.0,2022-01-24T13:40:53.817Z,bitFlyer,1643031653817
BTC/JPY,sell,0.09007266,3791092.0,2022-01-24T13:40:54.770Z,bitFlyer,1643031654770
BTC/JPY,sell,0.25,3791092.0,2022-01-24T13:40:54.783Z,bitFlyer,1643031654783
BTC/JPY,sell,0.06004844,3791092.0,2022-01-24T13:40:54.877Z,bitFlyer,1643031654877
BTC/JPY,sell,0.03956632,3791092.0,2022-01-24T13:40:55.073Z,bitFlyer,1643031655073
BTC/JPY,sell,0.02352,3791092.0,2022-01-24T13:40:55.543Z,bitFlyer,1643031655543
BTC/JPY,sell,0.1711,3791092.0,2022-01-24T13:40:55.697Z,bitFlyer,1643031655697
BTC/JPY,sell,0.1,3791092.0,2022-01-24T13:40:55.713Z,bitFlyer,1643031655713
BTC/JPY,sell,0.22646755,3791092.0,2022-01-24T13:40:55.730Z,bitFlyer,1643031655730
BTC/JPY,sell,0.01,3790973.0,2022-01-24T13:40:55.733Z,bitFlyer,1643031655733
BTC/JPY,sell,1.1,3790920.0,2022-01-24T13:40:55.733Z,bitFlyer,1643031655733
BTC/JPY,sell,0.0489,3790679.0,2022-01-24T13:40:55.733Z,bitFlyer,1643031655733
BTC/JPY,buy,0.001,3792561.0,2022-01-24T13:40:55.783Z,bitFlyer,1643031655783
BTC/JPY,buy,0.01,3792558.0,2022-01-24T13:40:56.637Z,bitFlyer,1643031656637
BTC/JPY,buy,0.0012,3794870.0,2022-01-24T13:40:57.177Z,bitFlyer,1643031657177
BTC/JPY,sell,0.01,3792940.0,2022-01-24T13:40:58.330Z,bitFlyer,1643031658330
```

# optional arguments:
##  -h, --help
show this help message and exit

## --exchanges [EXCHANGES [EXCHANGES ...]]
available exchanges: ['aax', 'aofex', 'ascendex',
'bequant', 'bibox', 'bigone', 'binance',
'binancecoinm', 'binanceus', 'binanceusdm', 'bit2c',
'bitbank', 'bitbay', 'bitbns', 'bitcoincom',
'bitfinex', 'bitfinex2', 'bitflyer', 'bitforex',
'bitget', 'bithumb', 'bitmart', 'bitmex', 'bitpanda',
'bitrue', 'bitso', 'bitstamp', 'bitstamp1', 'bittrex',
'bitvavo', 'bl3p', 'btcalpha', 'btcbox', 'btcmarkets',
'btctradeua', 'btcturk', 'buda', 'bw', 'bybit',
'bytetrade', 'cdax', 'cex', 'coinbase',
'coinbaseprime', 'coinbasepro', 'coincheck', 'coinex',
'coinfalcon', 'coinmarketcap', 'coinmate', 'coinone',
'coinspot', 'crex24', 'currencycom', 'delta',
'deribit', 'digifinex', 'eqonex', 'equos', 'exmo',
'flowbtc', 'ftx', 'ftxus', 'gateio', 'gemini',
'hitbtc', 'hitbtc3', 'hollaex', 'huobi', 'huobijp',
'huobipro', 'idex', 'independentreserve', 'indodax',
'itbit', 'kraken', 'kucoin', 'kuna', 'latoken',
'latoken1', 'lbank', 'liquid', 'luno', 'lykke',
'mercado', 'mexc', 'ndax', 'novadax', 'oceanex',
'okcoin', 'okex', 'okex3', 'okex5', 'paymium',
'phemex', 'poloniex', 'probit', 'qtrade', 'ripio',
'stex', 'therock', 'tidebit', 'tidex', 'timex',
'upbit', 'vcc', 'wavesexchange', 'whitebit', 'xena',
'yobit', 'zaif', 'zb', 'gmocoin']

## --symbols [SYMBOLS [SYMBOLS ...]]
an example of symbols: ['BTC/USD', 'ETH/USD',
'ETH/JPY', 'BTC/JPY', 'XRP/JPY']

## --out OUT
If value other than stdout, the log will be output under the specified directory.

## --loop LOOP
loop num. If 0, loop infinitely.
