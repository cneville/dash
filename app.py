# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import dash_bootstrap_components as dbc
import yfinance as yf
import matplotlib.pyplot as plt

# Initialize the app - incorporate a Dash Bootstrap theme
external_stylesheets = [dbc.themes.YETI]
app = Dash(__name__, external_stylesheets=external_stylesheets)

df_spc = yf.download (tickers = "^GSPC", start = "2016-01-01", 
                              end = "2019-09-01", interval = "1d")

df_spc['50ma'] = df_spc['Close'].rolling(window=50).mean()
df_spc['200ma'] = df_spc['Close'].rolling(window=200).mean()
df_spc = df_spc[['Close', '50ma', '200ma']]

fig = px.line(df_spc, x=df_spc.index, y=df_spc.columns)


app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
