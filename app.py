import feffery_antd_components as fac
import pandas as pd
from dash import Dash
from dash import html, dcc, Output, Input, callback
import dash_bootstrap_components as dbc
from server import app
from dash_echarts import DashECharts
from callbacks import callbacks
from views.plot import user_activation_plot


app.layout = dbc.Container([
    html.Div('header'),
    html.Div('用户维度'),
    dbc.Row([DashECharts(option=user_activation_plot(), id='user-activation day', style={'height': '250px'})]),
    dbc.Row(id='user-activation hour'),
    html.Div('商品维度'),
])


if __name__ == '__main__':
    app.run_server(debug=True)
