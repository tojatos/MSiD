import plotly.graph_objects as go
import pandas as pd

def plot(data):
    df = pd.DataFrame(data)
    print(df)

    fig = go.Figure(data=[go.Candlestick(x=df['time'],
                    open=df['open'],
                    high=df['high'],
                    low=df['low'],
                    close=df['close'])])

    fig.show()
