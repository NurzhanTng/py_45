import pandas as pd

# Создание двух DataFrame
df1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie']})
df2 = pd.DataFrame({'ID': [2, 3, 4], 'Salary': [60000, 75000, 80000]})

'''
# Внутреннее объединение (по умолчанию)
inner_merged = pd.merge(df1, df2, on='ID')

# Левое объединение
left_merged = pd.merge(df1, df2, on='ID', how='left')

# Правое объединение
right_merged = pd.merge(df1, df2, on='ID', how='right')

# Внешнее объединение
outer_merged = pd.merge(df1, df2, on='ID', how='outer')

print("Inner Merge:\n", inner_merged)
print("\nLeft Merge:\n", left_merged)
print("\nRight Merge:\n", right_merged)
print("\nOuter Merge:\n", outer_merged)
'''

# Объединение с дубликатами в ключевом столбце 'ID'
df3 = pd.DataFrame({'ID': [1, 2, 3], 'Value': ['X', 'Y', 'Z']})
duplicated_df = pd.concat([df1, df3], ignore_index=True)

print("Concatenated DataFrame with Duplicates:\n", duplicated_df)

# Обработка дубликатов при объединении
merged_with_duplicates = pd.merge(df1, df3, on='ID', how='outer', validate='one_to_many')

print("\nMerged DataFrame with Duplicates:\n", merged_with_duplicates)
