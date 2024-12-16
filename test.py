import pandas as pd
from models.api import API


data = API().user_activation()
data = pd.DataFrame.from_records(data, columns=['日期', '小时', '浏览', '收藏', '加购物车', '下单'])
data = data.to_dict('list')
print(data['日期'])