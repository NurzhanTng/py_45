import pandas as pd
import pandas as pd
import plotly.express as px

df = pd.read_csv('14/bitcoin.csv')
df.dropna(inplace=True)
del df['High'], df['Low'], df['Close'], df['Volume_(BTC)'], df['Volume_(Currency)'], df['Weighted_Price']
print(1)
df = df[df['Timestamp'] > 1617136500]
print(2)
df['Datetime'] = pd.to_datetime(df['Timestamp'])
fig = px.line(df, x = 'Datetime', y = 'Open', title='Changes of Bitcoin')
fig.show()