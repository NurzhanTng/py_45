import plotly.graph_objects as go

# Данные для графика
x_data = [1, 2, 3, 4]
y_data = [10, 11, 12, 13]

# Создаем линейный график
trace = go.Scatter(x=x_data, y=y_data, mode='lines')

# Собираем график
fig = go.Figure(trace)

# Отображаем график
print(1)
fig.show()
print(2)
