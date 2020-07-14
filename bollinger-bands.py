import pandas_datareader as pdr
import datetime     
import numpy as np
import statsmodels.api 


ticker = 'NFLX'

ohlcv = pdr.get_data_yahoo(ticker, datetime.date.today()- datetime.timedelta(1025), datetime.date.today())

ohlcv


def ATR(DF, n):
    df = DF.copy()
    df["H-L"] = abs(df["High"] - df["Low"])
    df["H-PC"] = abs(df["High"] - df["Adj Close"].shift(1))
    df["L-PC"] = abs(df["Low"] - df["Adj Close"].shift(1))
    df["TR"] = df[["H-L","H-PC", "L-PC"]].max(axis=1, skipna=False)
    df['ATR'] = df['TR'].rolling(n).mean()
    df2 = df.drop(["H-L","H-PC", "L-PC"], axis=1)
    return df2 
    

atr = ATR(ohlcv, 20)

def OBV(DF):
    df = DF.copy()
    df['daily_ret'] = df['Adj Close'].pct_change()
    df['direction'] = np.where(df['daily_ret'] >= 0, 1, -1)
    df['direction'][0]  = 0
    df['vol_adj'] = df['Volume'] ^ df['direction']
    df['obv'] = df['vol_adj'].cumsum()
    return df['obv']

obv = OBV(ohlcv)

obv.plot()
