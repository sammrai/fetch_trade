import ccxt as ccxt_
import time
from .gmocoin import gmocoin

# 同期
ccxt_.gmocoin = gmocoin

def fetch_ohlcv_my(self, *args, **kwargs):
    return self.fetch_ohlcv( *args, **kwargs)

class echo(object):
    def __getattr__(self, name, *args, **kwargs):
        x= getattr(ccxt_, name)
        x.fetch_ohlcv_ = fetch_ohlcv_my
        return x
ccxt=echo()

# 非同期
import ccxt.async_support as ccxt_async_
from .gmocoin_async import gmocoin as gmocoin_async
ccxt_async_.gmocoin = gmocoin_async

class echo_async(object):
    def __getattr__(self, name, *args, **kwargs):
        x= getattr(ccxt_async_, name)
        return x
ccxt_async=echo_async()