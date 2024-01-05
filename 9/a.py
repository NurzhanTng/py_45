import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data_json = pd.read_json('a.json')
# print(type(data_json['rating']))
# data_json.info()

s = pd.Series([1, 3, 5, np.nan, 6, 8])
# print(s[0])
# s[3] = 10
# print(s)
# print(s)


data = {
    'Имя': ['Анна', np.nan, 'Светлана'],
    'Возраст': [25, 30, 22],
    'Зарплата': [50000, 60000, 45000]
}

# df = pd.DataFrame(data)
# # print(df[df['Зарплата'] > 49_999])
# # df.info()
# print(df.head(), end='\n\n')
# print(df.tail(), end='\n\n')
# print(df.describe()['Возраст'])

""" OLD VERSION
import json

with open('a.json', 'r') as f:
    data = json.loads('\n'.join(f.readlines()))
    l = []
    for row in data:
        l.append(row['rating'])
    print(max(l))
"""

""" EXAMPLE OF NUMPY
import numpy as np

l = [4, 5, 6, 7, 8, 9, 10]
for i in range(len(l)):
    l[i] -= 4

print(l)

l = np.array(l)
print(l - 4)
"""

import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 6, 7])
arr_2D = np.array(np.array([
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 3, 4],
]))
arr3 = np.random.randint(0, 10, (3, 5))


x = np.linspace(-10, 10, 5)
y = np.array(
    [Xn**2 for Xn in x]
)
plt.plot(x, y)
plt.show()

# print(x)

# print(type(arr_2D))
# print(arr1 * 5)
