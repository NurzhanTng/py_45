import plotly.graph_objects as go

x_data = [1, 2, 3, 4]
y_data = [11, 12, 13, 14]

trace = go.Scatter(
    x=x_data,
    y=y_data,
    mode='markers'
)

fig = go.Figure(trace)

fig.update_layout(
    title='dafdfaf',
    xaxis_title='afefAA',
    yaxis_title='afefa'
)

fig.show()