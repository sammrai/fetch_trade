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
parser.add_argument('--loop', default=0, type=int)
parser.add_argument('--out', default="stdout", type=str, help="If value other than stdout, the log will be output under the specified directory.")

args = parser.parse_args()

exchanges = {e:{"rate_limit" : 1} for e in args.exchanges}
exchanges = [getattr(ccxt.ccxt_async,exchange)(keys) for exchange,keys in exchanges.items()]

keys=["time","open","high","low","close","volume"]
symbols=args.symbols

def xrange(range=0):
    c = 0
    while True:
        yield c
        c += 1
        if c==range:
            break

async def print_ohlcv(exchange, symbol):
    last_id=0
    for _ in xrange(args.loop):
        update = await exchange.fetch_trades(symbol=symbol,limit=100)
        update = pd.DataFrame(update).sort_index()
        update["exchange"]=exchange.name
        update["timestamp"]=update["timestamp"].astype("int")
        update = update.set_index("timestamp")
        update["timestamp"]=update.index
        update = update[["symbol","side","amount","price","datetime","exchange","timestamp"]]
        update = update[update.index>last_id]

        if len(update)>0:
            out = update.to_string(header=False,index=False)+"\n"
            last_id = update.index[-1]

            if args.out == "stdout":
                print(out,end="")
            else:
                date = datetime.now().strftime("%Y%m%d")
                fname = f"{exchange}_{symbol.replace('/','_')}_{date}.txt"
                fname = os.path.join(args.out,fname)
                with open(fname,"a") as f:
                    f.write(out)
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
        pass

    for exchange in exchanges:
        await exchange.close()

asyncio.get_event_loop().run_until_complete(main())