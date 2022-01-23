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
$ docker run --rm -u$(id -u) -v $(pwd)/data:/data  sammrai/fetch_trade  --exchanges gmocoin --symbols BTC/JPY --out /data

// gmocoin_BTC_JPY_20220123.txt
BTC/JPY  buy 0.01 4004113.0 2022-01-23T15:46:32.483Z gmocoin 16429527924830
BTC/JPY sell 0.02 4004607.0 2022-01-23T15:46:32.483Z gmocoin 16429527924831
BTC/JPY sell 0.01 4004113.0 2022-01-23T15:46:32.483Z gmocoin 16429527924831
BTC/JPY  buy 0.02 4005426.0 2022-01-23T15:46:35.455Z gmocoin 16429527954550
BTC/JPY  buy 0.03 4005398.0 2022-01-23T15:46:35.455Z gmocoin 16429527954550
BTC/JPY  buy 0.01 4005091.0 2022-01-23T15:46:35.455Z gmocoin 16429527954550
BTC/JPY  buy 0.01 4005000.0 2022-01-23T15:46:35.455Z gmocoin 16429527954550
BTC/JPY  buy 0.01 4004999.0 2022-01-23T15:46:35.455Z gmocoin 16429527954550
BTC/JPY  buy 0.01 4004851.0 2022-01-23T15:46:35.455Z gmocoin 16429527954550
BTC/JPY  buy 0.01 4004670.0 2022-01-23T15:46:35.455Z gmocoin 16429527954550
BTC/JPY sell 0.02 4005426.0 2022-01-23T15:46:35.455Z gmocoin 16429527954551
BTC/JPY sell 0.03 4005398.0 2022-01-23T15:46:35.455Z gmocoin 16429527954551
BTC/JPY sell 0.01 4005091.0 2022-01-23T15:46:35.455Z gmocoin 16429527954551
BTC/JPY sell 0.01 4005000.0 2022-01-23T15:46:35.455Z gmocoin 16429527954551
BTC/JPY sell 0.01 4004999.0 2022-01-23T15:46:35.455Z gmocoin 16429527954551
BTC/JPY sell 0.01 4004851.0 2022-01-23T15:46:35.455Z gmocoin 16429527954551
BTC/JPY sell 0.01 4004670.0 2022-01-23T15:46:35.455Z gmocoin 16429527954551
BTC/JPY  buy 0.02 4004019.0 2022-01-23T15:46:35.677Z gmocoin 16429527956770
BTC/JPY sell 0.02 4004019.0 2022-01-23T15:46:35.677Z gmocoin 16429527956771
BTC/JPY  buy 0.01 4003753.0 2022-01-23T15:46:36.657Z gmocoin 16429527966570
BTC/JPY sell 0.01 4003753.0 2022-01-23T15:46:36.657Z gmocoin 16429527966571
BTC/JPY  buy 0.01 4003391.0 2022-01-23T15:46:38.208Z gmocoin 16429527982080
BTC/JPY sell 0.01 4003391.0 2022-01-23T15:46:38.208Z gmocoin 16429527982081
BTC/JPY  buy 0.01 4003391.0 2022-01-23T15:46:41.572Z gmocoin 16429528015720
BTC/JPY sell 0.01 4003391.0 2022-01-23T15:46:41.572Z gmocoin 16429528015721
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
