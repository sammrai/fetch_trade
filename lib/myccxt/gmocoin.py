# -*- coding: utf-8 -*-

# PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
# https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

from ccxt import Exchange
from ccxt.base.errors import ExchangeError
from ccxt.base.errors import AuthenticationError
from ccxt.base.errors import PermissionDenied
from ccxt.base.errors import AccountSuspended
from ccxt.base.errors import ArgumentsRequired
from ccxt.base.errors import BadRequest
from ccxt.base.errors import InsufficientFunds
from ccxt.base.errors import InvalidOrder
from ccxt.base.errors import OrderNotFound
from ccxt.base.errors import OrderImmediatelyFillable
# from ccxt.base.errors import RateLimitExceeded
from ccxt.base.errors import InvalidNonce


class gmocoin(Exchange):

    def describe(self):
        return self.deep_extend(super(gmocoin, self).describe(), {
            'id': 'gmocoin',
            'name': 'gmocoin',
            'countries': ['JP'],
            'version': 'v1',
            'rateLimit': 300,
            'hostname': 'coin.z.com',
            'has': {
                'cancelAllOrders': True,
                'cancelOrder': True,
                'CORS': False,
                'createOrder': True,
                'createCloseOrders': True,
                'editOrder': True,
                'fetchBalance': True,
                'fetchClosedOrders': False,
                'fetchMarkets': False,
                'fetchMyTrades': True,
                'fetchOpenOrders': 'emulated',
                'fetchOrder': 'emulated',
                'fetchOrderBook': True,
                'fetchOrders': True,
                'fetchTicker': True,
                'fetchTrades': True,
            },
            'urls': {
                'logo': 'https://coin.z.com/corp_imgs/logo.svg',
                'api': {
                    'public': f'https://api.coin.z.com/public/v1',
                    'private': f'https://api.coin.z.com/private/v1',
                },
                'www': 'https://coin.z.com/jp',
                'doc': 'https://api.coin.z.com/docs',
                'fee': 'https://coin.z.com/jp/corp/guide/fees/',
            },
            'timeframes': {
                '1m': '1min',
                '5m': '5min',
                '10m': '10min',
                '15m': '15min',
                '30m': '30m',
                '1h': '1hour',
                '4h': '4hour',
                '8h': '8hour',
                '12h': '12hour',
                '1d': '1day',
                '1w': '1week',
                '1M': '1month',
            },
            'api': {
                'public': {
                    'get': [
                        'status',
                        'ticker',
                        'orderbooks',
                        'trades',
                        'klines'
                    ],
                },
                'private': {
                    'get': [
                        'account/margin',
                        'account/assets',
                        'orders',
                        'activeOrders',
                        'executions',
                        'latestExecutions',
                        'openPositions',
                        'positionSummary',
                    ],
                    'post': [
                        'order',
                        'changeOrder',
                        'cancelOrder',
                        'cancelOrders',
                        'cancelBulkOrder',
                        'closeOrder',
                        'closeBulkOrder',
                        'changeLosscutPrice',
                    ],
                },
            },
            'markets': {
                'BTC': {
                    'id': 'BTC',
                    'base': 'BTC',
                    'baseId': 'BTC',
                    'maker': -0.0001,
                    'quote': '',
                    'quoteId': '',
                    'spot': True,
                    'symbol': 'BTC',
                    'taker': 0.0005,
                },
                'ETH': {
                    'id': 'ETH',
                    'base': 'ETH',
                    'baseId': 'ETH',
                    'maker': -0.0001,
                    'quote': '',
                    'quoteId': '',
                    'spot': True,
                    'symbol': 'ETH',
                    'taker': 0.0005,
                },
                'BCH': {
                    'id': 'BCH',
                    'base': 'BCH',
                    'baseId': 'BCH',
                    'maker': -0.0001,
                    'quote': '',
                    'quoteId': '',
                    'spot': True,
                    'symbol': 'BCH',
                    'taker': 0.0005,
                },
                'LTC': {
                    'id': 'LTC',
                    'base': 'LTC',
                    'baseId': 'LTC',
                    'maker': -0.0001,
                    'quote': '',
                    'quoteId': '',
                    'spot': True,
                    'symbol': 'BCH',
                    'taker': 0.0005,
                },
                'XRP': {
                    'id': 'XRP',
                    'base': 'XRP',
                    'baseId': 'XRP',
                    'maker': -0.0001,
                    'quote': '',
                    'quoteId': '',
                    'spot': True,
                    'symbol': 'XRP',
                    'taker': 0.0005,
                },
                'BTC/JPY': {
                    'id': 'BTC_JPY',
                    'base': 'BTC',
                    'baseId': 'BTC',
                    'maker': 0.0,
                    'quote': 'JPY',
                    'quoteId': 'JPY',
                    'spot': False,
                    'symbol': 'BTC/JPY',
                    'taker': 0.0,
                },
                'ETH/JPY': {
                    'id': 'ETH_JPY',
                    'base': 'ETH',
                    'baseId': 'ETH',
                    'maker': 0.0,
                    'quote': 'JPY',
                    'quoteId': 'JPY',
                    'spot': False,
                    'symbol': 'ETH/JPY',
                    'taker': 0.0,
                },
                'BCH/JPY': {
                    'id': 'BCH_JPY',
                    'base': 'BCH',
                    'baseId': 'BCH',
                    'maker': 0.0,
                    'quote': 'JPY',
                    'quoteId': 'JPY',
                    'spot': False,
                    'symbol': 'BCH/JPY',
                    'taker': 0.0,
                },
                'LTC/JPY': {
                    'id': 'LTC_JPY',
                    'base': 'LTC',
                    'baseId': 'LTC',
                    'maker': 0.0,
                    'quote': 'JPY',
                    'quoteId': 'JPY',
                    'spot': False,
                    'symbol': 'LTC/JPY',
                    'taker': 0.0,
                },
                'XRP/JPY': {
                    'id': 'XRP_JPY',
                    'base': 'XRP',
                    'baseId': 'XRP',
                    'maker': 0.0,
                    'quote': 'JPY',
                    'quoteId': 'JPY',
                    'spot': False,
                    'symbol': 'XRP/JPY',
                    'taker': 0.0,
                },
                'XEM': {
                    'id': 'XEM',
                    'base': 'XEM',
                    'baseId': 'XEM',
                    'maker': 0.0,
                    'quote': 'JPY',
                    'quoteId': 'JPY',
                    'spot': False,
                    'symbol': 'XEM',
                    'taker': 0.0,
                },
            },
            'fees': {
                'trading': {
                    'maker': 0.0,
                    'taker': 0.0,
                },
                'BTC': {
                    'maker': -0.0001,
                    'taker': 0.0005,
                },
                'ETH': {
                    'maker': -0.0001,
                    'taker': 0.0005,
                },
                'BCH': {
                    'maker': -0.0001,
                    'taker': 0.0005,
                },
                'LTC': {
                    'maker': -0.0001,
                    'taker': 0.0005,
                },
                'XRP': {
                    'maker': -0.0001,
                    'taker': 0.0005,
                },
                'XEM': {
                    'maker': -0.0001,
                    'taker': 0.0005,
                },
            },
            # https://api.coin.z.com/docs/#status-code
            'exceptions': {
                'ERR-189': InvalidOrder,  # The quantity of your close order exceeds your open position.
                'ERR-200': InvalidOrder,  # There are existing active orders and your order exceeds the maximum quantity that can be ordered. Please change the quantity to order or cancel an active order in order to create a new close order.
                'ERR-201': InsufficientFunds,  # Insufficient funds.
                'ERR-208': InsufficientFunds,  # The quantity of your order exceeds your available balance. Please check your balance or active orders.
                'ERR-430': InvalidOrder,  # Invalid parameter (orderId/executionId) in executions.
                'ERR-554': ExchangeError,  # The server is unavalibale.
                'ERR-626': ExchangeError,  # The server is busy. Please retry later.
                'ERR-635': InvalidOrder,  # The number of active orders has exceeded the limit. Please cancel an active order to create a new order.
#                 'ERR-5003': RateLimitExceeded,  # The API usage limits are exceeded.
                'ERR-5008': InvalidNonce,  # The API-TIMESTAMP that is set in the request header is later than the system time of the API.
                'ERR-5009': InvalidNonce,  # The API-TIMESTAMP that is set in the request header is earlier than the system time of the API.
                'ERR-5105': InvalidOrder,  # Request parameter include mismatch type.
                'ERR-5106': ArgumentsRequired,  # The request parameter is invalid.
                'ERR-5012': AuthenticationError,  # The API authentication is invalid.
                'ERR-5014': AuthenticationError,  # The membership agreement has not been completed.
                'ERR-5115': InvalidOrder,  # The number of decimal digits is invalid.
                'ERR-5121': InvalidOrder,  # Impossible to order due to order price is too low.
                'ERR-5122': OrderImmediatelyFillable,  # The specified order can not be changed or canceled (already MODIFYING, CANCELLING, CANCELED, EXECUTED or EXPIRED). Orders can be changed or canceled only in ORDERED (WAITING for stop limit orders) status.
                'ERR-5123': OrderNotFound,  # The specified order doesn't exist.
                'ERR-5127': AccountSuspended,  # Your API connection is restricted.
                'ERR-5129': InvalidOrder,  # Stop limit orders cannot be specified a price that will be executed immediately.
                'ERR-5201': InvalidNonce,  # A response code that when Public/Private API is called while the service is in a regular maintenance.
                'ERR-5202': BadRequest,  # A response code that when Public/Private API is called while the service is in a emergency maintenance.
                'ERR-5203': BadRequest,  # A response code that when order or change order is called while the service is pre-open.
                'ERR-5204': BadRequest,  # The request API PATH is invalid.
                'ERR-5206': InvalidOrder,  # The limits of changing order for each order are exceeded. If you would like further changes for the order, please cancel the order and create a brand new order.
            },
        })

    def fetch_balance(self, params={}):
        self.load_markets()
        response = self.privateGetAccountAssets(params)
        # {
        #   "status": 0,
        #   "data": [
        #     {
        #       "amount": "993982448",
        #       "available": "993982448",
        #       "conversionRate": "1",
        #       "symbol": "JPY"
        #     },
        #     {
        #       "amount": "4.0002",
        #       "available": "4.0002",
        #       "conversionRate": "859614",
        #       "symbol": "BTC"
        #     }
        #   ],
        #   "responsetime": "2019-03-19T02:15:06.055Z"
        # }
        result = {'info': response}
        assets = self.safe_value(response, 'data', {})
        for i in range(0, len(assets)):
            balance = assets[i]
            currencyId = self.safe_string(balance, 'symbol')
            code = self.safe_currency_code(currencyId)
            account = self.account()
            account['total'] = self.safe_string(balance, 'amount')
            account['free'] = self.safe_string(balance, 'available')
            result[code] = account
        return self.parse_balance(result)

    def fetch_order_book(self, symbol, limit=None, params={}):
        self.load_markets()
        request = {
            'symbol': self.market_id(symbol),
        }
        response = self.publicGetOrderbooks(self.extend(request, params))
        # {
        #   "status": 0,
        #   "data": {
        #     "asks": [
        #       {
        #         "price": "455659",
        #         "size": "0.1"
        #       }
        #     ],
        #     "bids": [
        #       {
        #         "price": "455659",
        #         "size": "0.1"
        #       }
        #     ],
        #     "symbol": "BTC"
        #   },
        #   "responsetime": "2019-03-19T02:15:06.026Z"
        # }
        orderbook = self.safe_value(response, 'data', {})
        return self.parse_order_book(orderbook, None, 'bids', 'asks', 'price', 'size')

    def fetch_ticker(self, symbol, params={}):
        self.load_markets()
        request = {
            'symbol': self.market_id(symbol),
        }
        response = self.publicGetTicker(self.extend(request, params))
        # {
        #   "status": 0,
        #   "data": [
        #     {
        #       "ask": "750760",
        #       "bid": "750600",
        #       "high": "762302",
        #       "last": "756662",
        #       "low": "704874",
        #       "symbol": "BTC",
        #       "timestamp": "2018-03-30T12:34:56.789Z",
        #       "volume": "194785.8484"
        #     }
        #   ],
        #   "responsetime": "2019-03-19T02:15:06.014Z"
        # }
        data = self.safe_value(response, 'data', [])
        ticker = self.safe_value(data, 0, {})
        timestamp = self.parse8601(self.safe_string(ticker, 'timestamp'))
        last = self.safe_float(ticker, 'last')
        return {
            'symbol': symbol,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'high': self.safe_float(ticker, 'high'),
            'low': self.safe_float(ticker, 'low'),
            'bid': self.safe_float(ticker, 'bid'),
            'bidVolume': None,
            'ask': self.safe_float(ticker, 'ask'),
            'askVolume': None,
            'vwap': None,
            'open': None,
            'close': last,
            'last': last,
            'previousClose': None,
            'change': None,
            'percentage': None,
            'average': None,
            'baseVolume': self.safe_float(ticker, 'volume'),
            'quoteVolume': None,
            'info': ticker,
        }

    def parse_trade(self, trade, market=None):
        side = self.safe_string_lower(trade, 'side')
        if side is not None:
            if len(side) < 1:
                side = None
        order_id = self.safe_integer(trade, 'orderId')
        timestamp = self.parse8601(self.safe_string(trade, 'timestamp'))
        id = self.safe_integer(trade, 'executionId')
        if id is None:
            side_int = 0 if side=="buy" else 1
            id = int(timestamp)*10+side_int
        price = self.safe_float(trade, 'price')
        amount = self.safe_float(trade, 'size')
        cost = None
        fee = self.safe_float(trade, 'fee')
        if amount is not None:
            if price is not None:
                cost = price * amount
        symbol = None
        if market is not None:
            symbol = market['symbol']
        return {
            'id': id,
            'info': trade,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'symbol': symbol,
            'order': order_id,
            'type': None,
            'side': side,
            'takerOrMaker': None,
            'price': price,
            'amount': amount,
            'cost': cost,
            'fee': fee,
        }

    def fetch_trades(self, symbol, since=None, limit=None, params={}):
        self.load_markets()
        market = self.market(symbol)
        request = {
            'symbol': market['id'],
        }
        response = self.publicGetTrades(self.extend(request, params))
        # {
        #   "status": 0,
        #   "data": {
        #     "pagination": {
        #       "currentPage": 1,
        #       "count": 30
        #     },
        #     "list": [
        #       {
        #         "price": "750760",
        #         "side": "BUY",
        #         "size": "0.1",
        #         "timestamp": "2018-03-30T12:34:56.789Z"
        #       }
        #     ]
        #   },
        #   "responsetime": "2019-03-28T09:28:07.980Z"
        # }
        data = self.safe_value(response, 'data', {})
        trades = self.safe_value(data, 'list', [])
        return self.parse_trades(trades, market, since, limit)

    def create_order(self, symbol, type, side, amount, price=None, params={}):
        self.load_markets()
        request = {
            'symbol': self.market_id(symbol),
            'executionType': type.upper(),
            'side': side.upper(),
            'price': str(price),
        }
        if 'settlePosition' in params:
            params['settlePosition'] = [{
                'positionId': int(params['settlePosition']['positionId']),
                'size': str(params['settlePosition']['size'])
            }]
            response = self.privatePostCloseOrder(self.extend(request, params))
        else:
            request['size'] = str(amount)
            response = self.privatePostOrder(self.extend(request, params))
        # {
        #   "status": 0,
        #   "data": "637000",
        #   "responsetime": "2019-03-19T02:15:06.108Z"
        # }
        id = self.safe_string(response, 'data')
        return {
            'info': response,
            'id': id,
        }

    def create_close_orders(self, symbol, type, side, amount, price=None, params={}):
        self.load_markets()
        request = {
            'symbol': self.market_id(symbol),
            'side': side.upper(),
            'executionType': type.upper(),
            'price': str(price),
            'size': str(amount),
        }
        response = self.privatePostCloseBulkOrder(self.extend(request, params))
        # {
        #   "status": 0,
        #   "data": "637000",
        #   "responsetime": "2019-03-19T02:15:06.108Z"
        # }
        id = self.safe_string(response, 'data')
        return {
            'info': response,
            'id': id,
        }

    def cancel_order(self, id, symbol=None, params={}):
        self.load_markets()
        request = {
            'orderId': id,
        }
        response = self.privatePostCancelOrder(self.extend(request, params))
        # {
        #   "status": 0,
        #   "responsetime": "2019-03-19T01:07:24.557Z"
        # }
        return {
            'info': response,
        }

    def cancel_all_orders(self, symbol=None, params={}):
        if symbol is None:
            raise ArgumentsRequired(self.id + ' cancelAllOrders() requires a `symbol` argument')
        self.load_markets()
        market = self.market(symbol)
        request = {
            'symbols': [market['id']],
        }
        response = self.privatePostCancelBulkOrder(self.extend(request, params))
        # {
        #     "status": 0,
        #     "data": [637000,637002],
        #     "responsetime": "2019-03-19T01:07:24.557Z"
        # }
        ids = self.safe_value(response, 'data', [])
        return {
            'info': response,
            'ids': ids,
        }

    def parse_order_status(self, status, type):
        statuses = {
            'WAITING': 'pending',
            'ORDERED': 'open',
            'MODIFYING': 'modifying',
            'CANCELLING': 'canceling',
            'CANCELED': 'canceled',
            'EXECUTED': 'closed',
            'EXPIRED': 'expired',
        }
        if type=="stop" and status=="WAITING":
            status="ORDERED"
        return self.safe_string(statuses, status)

    def parse_order(self, order, market=None):
        timestamp = self.parse8601(self.safe_string(order, 'timestamp'))
        amount = self.safe_float(order, 'size')
        remaining = self.safe_float(order, 'size') - self.safe_float(order, 'executedSize')
        filled = self.safe_float(order, 'executedSize')
        price = self.safe_float(order, 'price')
        type = self.safe_string_lower(order, 'executionType')
        status = self.parse_order_status(self.safe_string(order, 'status'),type)
        side = self.safe_string_lower(order, 'side')
        marketId = self.safe_string(order, 'symbol')
        symbol = self.safe_symbol(marketId, market)
        timeInForce = self.safe_string(order, 'timeInForce')
        fee = None
        feeCost = None
        if feeCost is not None:
            fee = {
                'cost': feeCost,
                'currency': None,
                'rate': None,
            }
        id = self.safe_string(order, 'orderId')
        return {
            'id': id,
            'clientOrderId': None,
            'info': order,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'lastTradeTimestamp': None,
            'status': status,
            'symbol': symbol,
            'type': type,
            'timeInForce': timeInForce,
            'postOnly': None,
            'side': side,
            'price': price,
            'stopPrice': None,
            'cost': None,
            'amount': amount,
            'filled': filled,
            'remaining': remaining,
            'fee': fee,
            'average': None,
            'trades': None,
        }

    def fetch_orders(self, symbol=None, since=1, limit=100, params={}):
        if symbol is None:
            raise ArgumentsRequired(self.id + ' fetchOrders() requires a `symbol` argument.')
        self.load_markets()
        market = self.market(symbol)
        request = {
            'symbol': market['id'],
            'page': since,
            'count': limit,
        }
        response = self.privateGetActiveOrders(self.extend(request, params))
        # {
        #   "status": 0,
        #   "data": {
        #     "pagination": {
        #       "currentPage": 1,
        #       "count": 30
        #     },
        #     "list": [
        #       {
        #         "rootOrderId": 123456789,
        #         "orderId": 123456789,
        #         "symbol": "BTC",
        #         "side": "BUY",
        #         "orderType": "NORMAL",
        #         "executionType": "LIMIT",
        #         "settleType": "OPEN",
        #         "size": "1",
        #         "executedSize": "0",
        #         "price": "840000",
        #         "losscutPrice": "0",
        #         "status": "ORDERED",
        #         "timeInForce": "FAS",
        #         "timestamp": "2019-03-19T01:07:24.217Z"
        #       }
        #     ]
        #   },
        #   "responsetime": "2019-03-19T01:07:24.217Z"
        # }
        data = self.safe_value(response, 'data', {})
        orders = self.safe_value(data, 'list', [])
        return self.parse_orders(orders, market, since, limit)

    def fetch_open_orders(self, symbol=None, since=1, limit=100, params={}):
        response = self.fetch_orders(symbol, since, limit, params)
        open_oders = []
        for order in response:
            status = self.safe_string(order, 'status')
            if status in ['pending', 'open', 'modifying']:
                open_oders.append(order)
        return open_oders

    def fetch_order(self, id, symbol=None, params={}):
        if symbol is None:
            raise ArgumentsRequired(self.id + ' fetchOrders() requires a `symbol` argument.')
        self.load_markets()
        market = self.market(symbol)
        request = {
            'orderId': str(id),  # string
        }
        response = self.privateGetOrders(self.extend(request, params))
        # {
        #   "status": 0,
        #   "data": {
        #     "list": [
        #       {
        #         "orderId": 223456789,
        #         "rootOrderId": 223456789,
        #         "symbol": "BTC_JPY",
        #         "side": "BUY",
        #         "orderType": "NORMAL",
        #         "executionType": "LIMIT",
        #         "settleType": "OPEN",
        #         "size": "0.02",
        #         "executedSize": "0.02",
        #         "price": "1430001",
        #         "losscutPrice": "0",
        #         "status": "EXECUTED",
        #         "timeInForce": "FAS",
        #         "timestamp": "2020-10-14T20:18:59.343Z"
        #       },
        #       {
        #         "rootOrderId": 123456789,
        #         "orderId": 123456789,
        #         "symbol": "BTC",
        #         "side": "BUY",
        #         "orderType": "NORMAL",
        #         "executionType": "LIMIT",
        #         "settleType": "OPEN",
        #         "size": "1",
        #         "executedSize": "0",
        #         "price": "900000",
        #         "losscutPrice": "0",
        #         "status": "CANCELED",
        #         "cancelType": "USER",
        #         "timeInForce": "FAS",
        #         "timestamp": "2019-03-19T02:15:06.059Z"
        #       }
        #     ]
        #   },
        #   "responsetime": "2019-03-19T02:15:06.059Z"
        # }
        data = self.safe_value(response, 'data', {})
        orders = self.safe_value(data, 'list', [])
        order = self.safe_value(orders, 0, [])
        return self.parse_order(order, market)

    def fetch_my_trades(self, symbol=None, since=1, limit=100, params={}):
        if symbol is None:
            raise ArgumentsRequired(self.id + ' fetchMyTrades() requires a `symbol` argument')
        self.load_markets()
        market = self.market(symbol)
        request = {
            'symbol': market['id'],
            'page': since,
            'count': limit,
        }
        response = self.privateGetLatestExecutions(self.extend(request, params))
        # {
        #   "status": 0,
        #   "data": {
        #     "pagination": {
        #       "currentPage": 1,
        #       "count": 30
        #     },
        #     "list": [
        #       {
        #         "executionId": 72123911,
        #         "orderId": 123456789,
        #         "symbol": "BTC",
        #         "side": "BUY",
        #         "settleType": "OPEN",
        #         "size": "0.7361",
        #         "price": "877404",
        #         "lossGain": "0",
        #         "fee": "323",
        #         "timestamp": "2019-03-19T02:15:06.086Z"
        #       }
        #     ]
        #   },
        #   "responsetime": "2019-03-19T02:15:06.086Z"
        # }
        data = self.safe_value(response, 'data', {})
        trades = self.safe_value(data, 'list', [])
        return self.parse_trades(trades, market, since, limit)

    def fetch_positions(self, symbols=None, since=None, limit=None, params={}):
        if symbols is None:
            raise ArgumentsRequired(self.id + ' fetchPositions() requires a `symbols` argument.')
        self.load_markets()
        request = {
            'symbol': self.market_id(symbols),
        }
        # {
        #   "status": 0,
        #   "data": {
        #     "pagination": {
        #       "currentPage": 1,
        #       "count": 30
        #     },
        #     "list": [
        #       {
        #         "positionId": 1234567,
        #         "symbol": "BTC_JPY",
        #         "side": "BUY",
        #         "size": "0.22",
        #         "orderdSize": "0",
        #         "price": "876045",
        #         "lossGain": "14",
        #         "leverage": "4",
        #         "losscutPrice": "766540",
        #         "timestamp": "2019-03-19T02:15:06.094Z"
        #       }
        #     ]
        #   },
        #   "responsetime": "2019-03-19T02:15:06.095Z"
        # }
        response = self.privateGetOpenPositions(self.extend(request, params))
        data = self.safe_value(response, 'data', {})
        positions = self.safe_value(data, 'list', [])
        return positions

    def edit_order(self, id, symbol, type, side, amount=None, price=None, params={}):
        if price is None:
            raise ArgumentsRequired(self.id + ' editOrder() requires a `price` argument')
        request = {
            'orderId': int(id),
            'price': str(price),
        }
        response = self.privatePostChangeOrder(self.extend(request, params))
        # {
        #   "status": 0,
        #   "responsetime": "2019-03-19T01:07:24.557Z"
        # }
        return {
            'info': response,
        }

    def handle_errors(self, code, reason, url, method, headers, body, response, requestHeaders, requestBody):
        if code == 200:
            status = self.safe_integer(response, 'status')
            if status == 0:
                return
            else:
                errors = self.safe_value(response, 'messages', [])
                error = self.safe_value(errors, 0, {})
                error_code = self.safe_string(error, 'message_code')
                error_message = self.safe_string(error, 'message_string')
                raise self.exceptions[error_code]('Error: ' + self.id + ' ' + error_code + ' ' + error_message + str(requestBody))
        else:
            raise ExchangeError('Error: ' + self.id + ' ' + code + ' ' + body)

    def nonce(self):
        return self.milliseconds()

    def sign(self, path, api='public', method='GET', params={}, headers=None, body=None):
        endpoint = '/' + self.implode_params(path, params)
        url = self.urls['api'][api] + endpoint
        if method == 'GET' and params is not None:
            url += '?' + self.urlencode(params)
        if api == 'private':
            self.check_required_credentials()
            path = '/' + self.version + '/' + path
            nonce = str(self.nonce())
            text = nonce + method + path
            if method == 'POST':
                body = self.json(params)
                text = text + body

            signature = self.hmac(self.encode(text), self.encode(self.secret))
            headers = {
                'API-KEY': self.apiKey,
                'API-TIMESTAMP': nonce,
                'API-SIGN': signature
            }
        return {'url': url, 'method': method, 'body': body, 'headers': headers}

    def parse_ohlcv(self, ohlcv, market=None):
#         {'openTime': '1635886800000', 'open': '7195438', 'high': '7197254', 'low': '7194172', 'close': '7196066', 'volume': '1.1'}, 
        return [
            self.safe_integer(ohlcv, "openTime"),
            self.safe_number(ohlcv, "open"),
            self.safe_number(ohlcv, "high"),
            self.safe_number(ohlcv, "low"),
            self.safe_number(ohlcv, "close"),
            self.safe_number(ohlcv, "volume")]
    
    def fetch_ohlcv(self, symbol, timeframe='1m', since=None, limit=None, params={}):
        if since is None:
            since = self.milliseconds()-1*3600000

        self.load_markets()
        # GMOのAPIでは、指定日の前日21:00~指定日の21:00までが返ってくるため、
        # +3時間しなければ指定日のデータが取得できない。
        # 例：11/3の22:00を指定した場合は、11/3の21:00~11/3の21:00しか取得できないため、11/4のデータとして取得する必要がある。
        request = {
            'symbol': self.market_id(symbol),
            "interval":self.timeframes[timeframe],
            "date":self.ymd(since+3*3600000,infix="")
        }
#         [[1635950400000,
#           7072569.0,
#           7072569.0,
#           7067513.0,
#           7067513.0,
#           0.9800000000000006],
#          [1635950460000,
#           7069578.0,
#           7069614.0,
#           7067425.0,
#           7067425.0,
#           0.18000000000000005],
#          [1635950520000,
#           7065801.0,
#           7065801.0,
#           7063569.0,
#           7065670.0,
#           0.9700000000000004]]

        response = self.public_get_klines(self.extend(request, params))
        data = self.safe_value(response, 'data', {})
        return self.parse_ohlcvs(data, self.market(symbol), timeframe, since, limit)



