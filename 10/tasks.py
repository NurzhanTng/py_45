import pandas as pd

# Создание DataFrame с информацией о продажах
sales_data = {'Product': ['A', 'B', 'A', 'B', 'A', 'B'],
              'Region': ['North', 'South', 'East', 'West', 'North', 'South'],
              'Sales': [100, 150, 120, 200, 180, 220]}

sales_df = pd.DataFrame(sales_data)

'''
# Задача 1: Найти средние продажи по каждому продукту

# Задача 2: Отсортировать данные по продажам в порядке убывания

# Задача 3: Объединить данные с дополнительной информацией
additional_info = {'Product': ['A', 'B'], 'Category': ['Category_X', 'Category_Y']}
'''