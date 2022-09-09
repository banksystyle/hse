import pandas as pd
import random

df = pd.read_csv('tz_data.csv', usecols=['area', 'cluster', 'cluster_name', 'keyword', 'x', 'y', 'count'])
#удаление пустых строк
df.dropna(inplace=True)

#удаление строк с некорректными значениями
df.drop(df[df['count'].apply(pd.to_numeric, errors="coerce").isna()].index, inplace=True)
df.drop(df[df['y'].apply(pd.to_numeric, errors="coerce").isna()].index, inplace=True)
df['count'] = pd.to_numeric(df['count'])
df['y'] = pd.to_numeric(df['y'])

#Удаление дубликатов
df.drop(df[df[['area', 'keyword']].duplicated()].index, inplace=True)

#создание набора цветов для каждого area
lst_color = ['#9edae5', '#17becf', '#dbdb8d', '#bcbd22', '#c7c7c7', '#7f7f7f', '#f7b6d2', '#e377c2', '#c49c94', '#8c564b', '#c5b0d5', '#9467bd', '#ff9896', '#d62728', '#98df8a', '#2ca02c', '#ffbb78', '#ff7f0e', '#aec7e8', '#1f77b4']
dct = {}

for area in df.area.unique():
    color = random.sample(lst_color, k=len(area))
    dct[area] = {name:color[num] for num, name in enumerate(df.cluster_name.unique())}

#добавление столбца color
df['color'] = df[['area', 'cluster_name']].apply(lambda x: dct[x[0]][x[1]], axis=1)

#сортировка
res = df.sort_values('count', ascending=False).sort_values(['area', 'cluster', 'cluster_name'])

#экспорт в формат excel
res.to_excel('table.xlsx', index=False)
