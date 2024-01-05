"""
import pandas as pd

# Создание DataFrame
data = {'Category': ['A', 'B', 'A', 'B', 'A', 'B'],
        'Value': [10, 15, 20, 25, 30, 35]}

df = pd.DataFrame(data)
grouped_df = df.groupby('Category')
print(grouped_df)
print(grouped_df.sum())
"""

import pandas as pd
import matplotlib.pyplot as plt
import psycopg2 as pg
import pandas.io.sql as psql

connection = pg.connect("host=localhost dbname=ict user=ictuser password=qwerty90")
df = psql.read_sql('SELECT * FROM salary_dataset', connection)

df_copy = df.copy()
del df_copy['id'], df_copy['age'], df_copy['gender'], df_copy['experience'], df_copy['education_level']
grouped_df = df_copy.groupby('job_title')
mean_salary_by_job = grouped_df.mean()
print(mean_salary_by_job.sort_values(by='salary', ascending=False).head(15), end='\n\n\n\n')

df_copy = df[df['experience'] > 10].copy()
del df_copy['id'], df_copy['age'], df_copy['gender'], df_copy['experience'], df_copy['education_level']
grouped_df = df_copy.groupby('job_title')
mean_salary_by_job = grouped_df.mean()
print(mean_salary_by_job.sort_values(by='salary', ascending=False).head(15))

# print(df)

'''
3 4 8 9 10
mean() -> 3+4+8+9+10 / 5 = 6.8
median() -> 8
'''