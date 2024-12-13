import os
import dash
from dash import html, dcc
from flask import request, send_from_directory
import dash_bootstrap_components as dbc
from assets.cfg import *


# 实例化应用
app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    external_stylesheets=[
       'https://cdn.staticfile.org/twitter-bootstrap/4.5.2/css/bootstrap.min.css',
       dbc.themes.BOOTSTRAP,
       dbc.icons.BOOTSTRAP,
    ],
    use_pages=True
)

# 数据库配置
app.server.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}"
app.server.config["SQLALCHEMY_ECHO"] = True
app.server.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
ctx = app.server.app_context()
ctx.push()


