import pandas as pd
import pymysql


class API:
    def __init__(self):
        self.conn = pymysql.connect(
            host='localhost',
            user='root',
            password='123456',
            port=3306,
            db='data',
            charset='utf8'
        )
        self.cur = self.conn.cursor()

    def user_activation(self, grainSize):
        match grainSize:
            case 'day' | 'Day':
                sql = '''select Date, sum(surf) as surf, sum(fav) as fav, sum(cart) as cart, sum(buy) as buy from user_activation group by Date'''
            case 'hour' | 'Hour':
                sql = '''select Hour, sum(surf) as surf, sum(fav) as fav, sum(cart) as cart, sum(buy) as buy from user_activation group by Hour'''
            case 'mix':
                sql = '''select * from user_activation'''
        self.cur.execute(sql)
        data = self.cur.fetchall()
        return data
