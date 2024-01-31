import pandas as pd

data = {
    'Дата': ['2023-01-01 12:00:00', '2023-01-02 08:23:40', '2023-01-10 09:00:00']
}

df = pd.DataFrame(data)
df['Дата'] = pd.to_datetime(df['Дата'])
df['Дата 2'] = df['Дата'].dt.strftime('%m/%d/%Y')

print(df)
