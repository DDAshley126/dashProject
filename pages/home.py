import pandas as pd
from dash import html
import dash
import numpy as np
import dash_bootstrap_components as dbc


dash.register_page(__name__, path='/')

layout = dbc.Container(
    [
        html.Div('Home'),
    ]
)