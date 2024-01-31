import plotly.express as px
df = px.data.tips()
# print(df.info())
# df.to_csv('14/b_input.csv', encoding='utf-8')
fig = px.histogram(df, x="total_bill", color='sex')
fig.update_layout(bargap=0.2)
fig.show()
