from ast import arg
from datetime import datetime
import myccxt as ccxt
import asyncio
import argparse
import time
import pandas as pd
import os

parser = argparse.ArgumentParser(description='an ohlcv fetcher.')
parser.add_argument('--exchanges', required=True, nargs="*", type=str) 
parser.add_argument('--symbols', required=True, nargs="*", type=str)
parser.add_argument('--dir', default="./", type=str)
args = parser.parse_args()

exchanges = {e:{"rate_limit" : 1} for e in args.exchanges}
exchanges = [getattr(ccxt.ccxt_async,exchange)(keys) for exchange,keys in exchanges.items()]

keys=["time","open","high","low","close","volume"]
symbols=args.symbols


async def print_ohlcv(exchange, symbol):
    last_id=0
    while True:
        update = await exchange.fetch_trades(symbol=symbol,limit=100)
        update = pd.DataFrame(update).sort_index()
        update = update.set_index("id")
        update["exchange"]=exchange.name
        update["id"]=update.index.astype("int")
        update = update[["symbol","side","amount","price","datetime","exchange","id"]]
        update = update[update.index>last_id]

        if len(update)>0:
            date = datetime.now().strftime("%Y%m%d")
            fname = f"{exchange}_{symbol.replace('/','_')}_{date}.txt"
            fname = os.path.join(args.dir,fname)
            last_id = update.index[-1]
            with open(fname,"a") as f:
                s = update.to_string(header=False,index=False)+"\n"
                f.write(s)
        time.sleep(1)

async def main():
    cors=[]
    for exchange in exchanges:
        await exchange.load_markets()

        for symbol in symbols:
            if symbol not in exchange.symbols : continue
            cors.append(print_ohlcv(exchange,symbol=symbol))

    try:
        await asyncio.gather(*cors)
    except KeyboardInterrupt:
        for exchange in exchanges:
            await exchange.close()

asyncio.get_event_loop().run_until_complete(main())