import dash
import feffery_antd_components as fac
from dash import Dash
from dash import html, dcc, Output, Input, callback
import feffery_utils_components as fuc
import dash_bootstrap_components as dbc
from server import app
from models import api
from callbacks import callbacks


app.layout = html.Div([
    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        multiple=True
    ),
    html.Div(id='output-data-upload'),
])


if __name__ == '__main__':
    app.run_server(debug=True)
