import pandas as pd

data = pd.read_csv('./dataset/behavior_data.csv')
for i in data.values:
    print(i[0])