import pandas as pd

# Пустой акпаратты оширу
# df = pd.read_excel('11/Titanic_dataset.xlsx', 'titanic3')

# print(f'Канша акпары жок: \n{df.isnull().sum()}\n\n')

# df['age'].fillna(df['age'].mean(), inplace=True)
# print(f'Канша акпары жок: \n{df.isnull().sum()}')

# df.dropna(axis=0, inplace=True) # строка
# df.dropna(axis=0, inplace=True) # колонка

# print(f'Канша акпары жок: \n{df.isnull().sum()}\n\n')



# Изменение типа
# df['age'] = pd.to_numeric(df['age'])
# print(df.info())


# print(len(df[df['age'].apply(lambda x: x > 50)]))
# print(len(df))

# print(df[df['age'].apply(lambda x: x > 50)]['age'])

def filter_by_salary(salary):
    return lambda x: x['salary'] > salary

df = pd.read_csv('11/Salary_Data2.csv')
# print(df[df['age'].apply(filter_by_salary(240_000), axis=1)])

def categorize_age(age):
    if age < 30:
        return 'Young'
    elif 30 <= age < 40:
        return 'Middle age'
    else:
        return 'Senior'

# df['age_category'] = df['age'].apply(categorize_age)
# print(df[df.apply(filter_by_salary(200_000), axis=1)])
# print(df)
n = df.to_numpy()
# print(n[0][1])