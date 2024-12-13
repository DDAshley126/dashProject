import feffery_antd_components as fac
import pandas as pd
from dash import Dash
from dash import html, dcc, Output, Input, callback
import dash_bootstrap_components as dbc
from server import app
from models import api
from callbacks import callbacks


data = pd.read_csv('./dataset/behavior_data.csv')
app.layout = html.Div([
    fac.AntdTable(
        columns=[
            {
                'title': '用户ID',
                'dataIndex': '用户ID'
            },
            {
                'title': '商品ID',
                'dataIndex': '商品ID'
            },
            {
                'title': '类别ID',
                'dataIndex': '类别ID'
            },
            {
                'title': '行为ID',
                'dataIndex': '行为ID'
            },
            {
                'title': '时间',
                'dataIndex': '时间'
            },
        ],
        data=data.to_dict('records'),
        pagination={'pageSize': '5'}
    )
])


if __name__ == '__main__':
    app.run_server(debug=True)
