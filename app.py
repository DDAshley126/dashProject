import dash
import feffery_antd_components as fac
from dash import Dash
from dash import html, dcc, Output, Input, callback
import dash_bootstrap_components as dbc
from server import app
from models import api
from callbacks import callbacks


app.layout = html.Div([
    html.Div(id='output-data-upload'),
])


if __name__ == '__main__':
    app.run_server(debug=True)
