import pandas as pd

df = pd.DataFrame({
      'country': ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine'],
      'population': [17.04, 143.5, 9.5, 45.5],
      'square': [2724902, 17125191, 207600, 603628]
})


print(df)

print('---------')

print(df['country'])

print('---------')

print(type(df['country']))

print('---------')
# Объект DataFrame имеет 2 индекса: по строкам и по столбцам
print(df.columns)
print(df.index)

# Доступ по индексу в DataFrame

df = pd.DataFrame({
     'country': ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine'],
     'population': [17.04, 143.5, 9.5, 45.5],
     'square': [2724902, 17125191, 207600, 603628]
}, index=['KZ', 'RU', 'BY', 'UA'])

print(df)
print('---------')

df.index = ['KZ', 'RU', 'BY', 'UA']
df.index.name = 'Country Code'
print(df)
print('---------')

# Доступ к строкам по индексу возможен несколькими способами:
# .loc - используется для доступа по строковой метке
# .iloc - используется для доступа по числовому значению (начиная от 0)

print(df.loc['KZ'])

print('---------')

print(df.iloc[0])

print('---------')

# делать выборку по индексу и интересующим колонкам
print(df.loc[['KZ', 'RU'], 'population'])

print('---------')
# Фильтровать DataFrame с помощью т.н. булевых массивов
print(df[df.population > 10][['country', 'square']])

print('---------')

print(df.loc['KZ':'BY', :])

print('---------')
# Сбросить индексы
print(df.reset_index())

# Добавим новый столбец, в котором население (в миллионах) поделим на площадь страны, получив тем самым плотность
df['density'] = df['population'] / df['square'] * 1000000
print(df)

print('---------')
# удалить столбец
print(df.drop(['density'], axis='columns'))

print('---------')
# Переименовывать столбцы
print(df.rename(columns={'Country Code': 'country_code'}))
