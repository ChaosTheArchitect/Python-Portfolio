import yfinance as yf
import datetime as dt
import plotly.graph_objects as go
from plotly.subplots import make_subplots

start = dt.datetime(2020, 1, 1)
end = dt.datetime.now()

cryptos = ["ETH-USD", "ADA-USD", "ATOM-USD"]

# Create a subplot layout: 1 row for 3D chart + 1 row for each crypto
fig = make_subplots(rows=len(cryptos) + 1, cols=1,
                    shared_xaxes=True,
                    vertical_spacing=0.1,
                    subplot_titles=cryptos,
                    row_heights=[0.8] + [0.2/len(cryptos)]*len(cryptos),  # 60/40 split
                    specs=[[{"type": "scatter3d"}]] + [[{"type": "xy"}]]*len(cryptos))

# Add 3D chart to the first row
for ticker in cryptos:
    data = yf.download(ticker, start=start, end=end)
    fig.add_trace(go.Scatter3d(
        x=data.index,
        y=[ticker] * len(data),
        z=data['Close'].values,
        mode='markers',
        marker=dict(size=3),
        name=ticker,
        showlegend=False
    ), row=1, col=1)

# Add candlestick charts to subsequent rows
for idx, crypto in enumerate(cryptos, start=2):  # start=2 because row=1 is for 3D chart
    data = yf.download(crypto, start=start, end=end)
    fig.add_trace(go.Candlestick(
        x=data.index,
        open=data['Open'],
        high=data['High'],
        low=data['Low'],
        close=data['Close'],
        name=crypto,
        showlegend=False
    ), row=idx, col=1)

fig.update_layout(title="Crypto Analysis")
fig.show()
