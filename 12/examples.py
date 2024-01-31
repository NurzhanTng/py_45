import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame({
    'дата': pd.date_range(start='2022-01-01', end='2022-01-10'),
    'значение': [3, 7, 1, 10, 5, 8, 4, 6, 9, 2]
})

# plt.plot(df['дата'], df['значение'])
# plt.bar(df['дата'], df['значение'])
# plt.pie(df['значение'], labels=df['дата'], colors=['blue', 'orange', 'green'])
plt.title('Временное распределение значений')
plt.xlabel('Дата')
plt.ylabel('Значение')
plt.show()