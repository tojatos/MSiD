import plotly.graph_objects as go
from plotly.subplots import make_subplots

def plot(df):
    fig = make_subplots(rows=1, cols=2)
    fig.add_trace(
        go.Candlestick(
            name='Stock prices',
            x=df['time'],
            open=df['open'],
            high=df['high'],
            low=df['low'],
            close=df['close'],
        ),
        row=1, col=1,
    )
    fig.add_trace(
        go.Bar(
            name='Percentage change',
            x=df['time'],
            y=df['per_ch'],
        ),
        row=1, col=2,
    )

    fig.show()
