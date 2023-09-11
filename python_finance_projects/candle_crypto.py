import pandas_datareader as web
import datetime as dt
import plotly.graph_objects as go

start = dt.datetime(2020, 1, 1)
end = dt.datetime.now()

cryptos = ["ETH-USD", "ADA-USD", "ATOM-USD"]

for crypto in cryptos:
    data = web.DataReader(crypto, "yahoo", start, end)

    fig = go.Figure(data=[go.Candlestick(
        x=data.index,
        open=data['Open'],
        high=data['High'],
        low=data['Low'],
        close=data['Close'],
        name=crypto
    )])

    fig.update_layout(title=crypto)
    fig.show()
