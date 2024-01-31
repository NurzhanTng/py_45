import pandas as pd
import matplotlib.pyplot as plt
import psycopg2 as pg
import pandas.io.sql as psql

connection = pg.connect("host=localhost dbname=ict user=ictuser password=qwerty90")
dataframe = psql.read_sql('SELECT * FROM salary_dataset', connection)
dataframe['salary'].fillna(dataframe['salary'].mean(), inplace=True)
dataframe.dropna(inplace=True)
dataframe.drop_duplicates(inplace=True)
print(dataframe.info())
dataframe['salary'].plot(kind='hist', bins=100, edgecolor='black')
plt.legend()
plt.show()

# df = pd.read_csv('Salary_Data2.csv')
# print(df[df['age'] == 52])
# df2 = pd.read_excel('file.xlsx', sheet_name='Sheet1')
# print(df.describe())

df = pd.DataFrame([[1,'Bob', 'Builder'],
                  [2,'Sally', 'Baker'],
                  [3,'Scott', 'Candle Stick Maker']], 
columns=['id','name', 'occupation'])