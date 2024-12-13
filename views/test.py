# from dash import Dash, html, dcc, Output, Input
# import dash_bootstrap_components as dbc
# import dash
# from server import app


# app.layout = html.Div(
#     [
#         dcc.Location(id='url'),
#         html.Div([
#             html.Div(html.H3('dashboard')),
#         ]),
#         html.Hr(),
#         dbc.Nav(
#             [
#                 dbc.NavLink('Home', href='/', active='exact'),
#                 dbc.NavLink('first', href='/1', active='exact'),
#             ],
#             vertical=True,
#             pills=True,
#         ),
#         html.Div(id='page-content', style={'flex': 'auto'}),
#     ]
# )


# @app.callback(
#     Output('page-content', 'children'),
#     Input('url', 'pathname'),
# )
# def render_page_content(pathname):
#     if pathname == '/':
#         return index_page
#     elif pathname == '/1':
#         return age_page
#     else:
#         return html.H1('404')

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine, inspect, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Float


engine = create_engine('mysql+pymysql://root:123456@localhost:3306/dashboard_dash')
# insp = inspect(engine)
# Base = automap_base()
# Base.prepare(engine, reflect=True)
# tables = Base.classes.keys()
# user = Base.classes.channel_dwd
# metadata = MetaData()
# metadata.reflect(schema='test', bind=engine)
# keys = user.__table__.columns.keys()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3306/dashboard_dash'
db = SQLAlchemy(app)
# Session = sessionmaker(bind=engine)
# session = Session()


class channelDWD(db.Model):
    __tablename__ = 'channel_dwd'

    date = Column(String, primary_key=True)
    year_and_month = Column(String, nullable=False)
    post_amount = Column(Integer)
    wechat_amount = Column(Integer)
    on_delivery = Column(Integer)
    income = Column(Float)

    def __repr__(self):
        return "User object:%s" % self.date


result = channelDWD.query.get()
for record in result:
    print(record.year_and_month, record.income)

