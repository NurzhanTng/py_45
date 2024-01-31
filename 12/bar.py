import matplotlib.pyplot as plt


categories = ['A', 'B', 'C', 'D']
values = [3, 7, 2, 5]

plt.bar(categories, values)
plt.text(3, 7, 'Пример текста', fontsize=12, color='blue')
plt.show()