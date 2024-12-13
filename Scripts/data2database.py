import pandas as pd
import pymysql


class Import2Mysql:
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

    def __del__(self):
        self.cur.close()

    def write2mysql(self):
        data = pd.read_csv('../dataset/behavior_data.csv')
        for i in data.values:
            sql = f'''
                insert into `test`.`user_behavior`(`UserID`, `ItemID`, `CategoryID`, `BehaviorType`, `Timestamp`) values ('{i[0]}', '{i[1]}', '{i[2]}', '{i[3]}', '{i[4]}');
            '''
            self.cur.execute(sql)
            self.conn.commit()
        print('数据导入完成')

    def create(self):
        # 若已存在表，则删除
        drop_table = 'drop table if exists user_behavior;'
        self.cur.execute(drop_table)

        # 创建表
        create_table = '''
            create table `user_behavior` (
                `UserID` varchar(255) not null comment '用户ID',
                `ItemID` varchar(255) not null comment '商品ID',
                `CategoryID` varchar(255) not null comment '种类ID',
                `BehaviorType` varchar(255) not null comment '行为种类',
                `Timestamp` varchar(255) not null comment '时间'
            ) engine=InnoDB
        '''
        self.cur.execute(create_table)
        self.conn.commit()

    def run(self):
        self.create()
        self.write2mysql()


if __name__ == '__main__':
    Import2Mysql().run()
