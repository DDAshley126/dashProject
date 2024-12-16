from models.api import API
import pandas as pd


def user_activation_plot():
    data = API().user_activation('day')
    data = pd.DataFrame.from_records(data, columns=['日期', '浏览', '收藏', '加购物车', '下单'])
    option = {
        'title': {
            'text': '用户活跃度分析',
            'subtext': '粒度-天'
        },
        'tooltip': {
            'trigger': 'axis',
            'axisPointer': {
                'type': 'cross'
            }
        },
        'toolbox': {
            'show': True,
            'feature': {
                'saveAsImage': {}
            }
        },
        'xAxis': {
            'type': 'category',
            'boundaryGap': False,
            'data': data
        },
        'visualMap': {
            'show': False,
            'dimension': 0,
            'pieces': [
                {
                    'lte': 6,
                    'color': 'green'
                },
            ]
        },
        'series': [
            {
                'name': 'Electricity',
                'type': 'line',
                'smooth': True,
                'data': [300, 280, 250, 260, 270, 300, 550, 500, 400, 390, 380, 390, 400, 500, 600, 750, 800, 700, 600,
                         400],
                'markArea': {
                    'itemStyle': {
                        'color': 'rgba(255, 173, 177, 0.4)'
                    },
                    'data': [
                        [
                            {
                                'name': 'Morning Peak',
                                'xAxis': '07:30'
                            },
                            {
                                'xAxis': '10:00'
                            }
                        ],
                    ]
                }
            }
        ]
    }
    return option