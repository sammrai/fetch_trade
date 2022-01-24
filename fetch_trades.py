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
parser.add_argument('--reflesh_rate', default=5, type=int)

args = parser.parse_args()

exchanges = {e:{} for e in args.exchanges}
exchanges = [getattr(ccxt.ccxt_async,exchange)(keys) for exchange,keys in exchanges.items()]

def xrange(range=0):
    c = 0
    while True:
        yield c
        c += 1
        if c==range:
            break

def get_last_id(fname):
    try:
        df = pd.read_csv(fname,header=None)
        return df[6].values[-1]
    except:
        return 0

def get_fname(out, exchange, symbol):
    date = datetime.now().strftime("%Y%m%d")
    fname = f"{exchange.name}_{symbol.replace('/','_')}_{date}.txt"
    fname = os.path.join(out,fname)
    return fname

async def print_ohlcv(exchange, symbol):
    # resume last id when file exists.
    last_id = get_last_id(get_fname(args.out, exchange, symbol))

    for _ in xrange(args.loop):
        try:
            update = await exchange.fetch_trades(symbol=symbol,limit=100)
        except Exception as e:
            print(f"WARNING: {e}")
            continue
        update = pd.DataFrame(update).sort_index()
        update["exchange"]=exchange.name
        update["timestamp"]=update["timestamp"].astype("int")
        update = update.set_index("timestamp")
        update["timestamp"]=update.index
        update = update[["symbol","side","amount","price","datetime","exchange","timestamp"]]
        update = update[update.index>last_id]

        if len(update)>0:
            out = update.to_csv(index=False, header=False, sep=',')
            last_id = update.index[-1]

            if args.out == "stdout":
                print(out,end="")
            else:
                fname=get_fname(args.out, exchange, symbol)
                with open(fname,"a") as f:
                    f.write(out)
        time.sleep(args.reflesh_rate)

async def main():
    cors=[]
    for exchange in exchanges:
        await exchange.load_markets()

        for symbol in args.symbols:
            if symbol not in exchange.symbols :
                print(f"WARNING {symbol} is not supoport on {exchange.name}")
                continue
            cors.append(print_ohlcv(exchange,symbol=symbol))

    try:
        await asyncio.gather(*cors)
    except KeyboardInterrupt:
        pass

    for exchange in exchanges:
        await exchange.close()

asyncio.get_event_loop().run_until_complete(main())