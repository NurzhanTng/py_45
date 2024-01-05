'''
> < == !=

& - and
| - or
~ - not
'''

import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 25],
        'Salary': [50000, 60000, 75000, 55000]}

df = pd.DataFrame(data)

filtered_df = df[(df['Age'] >= 25) & (df['Salary'] < 70_000)]
# print(filtered_df)

sorted_df = df.sort_values(by=['Age', 'Salary'], ascending=False)
print(sorted_df)

# filtered_df = df[df['Age'] >= 30]
# print(filtered_df)