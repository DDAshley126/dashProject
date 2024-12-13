#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：dashProject 
@File    ：page1.py
@IDE     ：PyCharm 
@Author  ：Du Manting
@Date    ：2024/10/16 14:58 
'''

import pandas as pd
from dash import html
import dash
import numpy as np
import dash_bootstrap_components as dbc
# from models.Models import Order, query2dict



dash.register_page(__name__, path='/page1')
layout = dbc.Container(
    [
        html.H3('广州外呼'),
        # html.Div(data[0].amount)
    ]
)
