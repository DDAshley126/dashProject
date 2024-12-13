from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine, inspect, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Float


engine = create_engine('mysql+pymysql://root:123456@localhost:3306/dashboard_dash')
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

