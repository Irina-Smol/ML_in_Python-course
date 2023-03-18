import pandas as pd

my_series = pd.Series([5, 6, 7, 8, 9, 10])
print(my_series)

print('---------')

print(my_series.index)
print(my_series.values)

print('---------')

print(my_series[4])

print('---------')
# индексы можно задавать явно
my_series2 = pd.Series([5, 6, 7, 8, 9, 10], index=['a', 'b', 'c', 'd', 'e', 'f'])
print(my_series2['f'])

print('---------')

# выборкa по нескольким индексам и групповое присваивание
print(my_series2[['a', 'b', 'f']])

print('---------')

print(my_series2[my_series2 > 0] * 2)

print('---------')

# Если Series напоминает нам словарь, где ключом является индекс, а значением сам элемент, то можно сделать так
my_series3 = pd.Series({'a': 5, 'b': 6, 'c': 7, 'd': 8})
print(my_series3)
print('d' in my_series3)

print('---------')

# У объекта Series и его индекса есть атрибут name, задающий имя объекту и индексу соответственно
my_series3.name = 'numbers'
my_series3.index.name = 'letters'
print(my_series3)

# Индекс можно поменять "на лету", присвоив список атрибуту index объекта Series
my_series3.index = ['A', 'B', 'C', 'D']
print(my_series3)