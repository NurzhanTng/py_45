# import matplotlib.pyplot as plt
# import numpy as np

# x = np.array([1, 3, 4, 6])
# y = np.array([3, 8, 1, 10])
# plt.plot(x, y, 'o:b')
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np

# ypoints = np.array([3, 8, 1, 10])

# plt.plot(ypoints, marker = 'o', ms = 90, mec = 'r', mfc='g')
# plt.grid(axis='x')
# plt.show()

import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from time import time
# print((datetime.now() - timedelta(days=3*365)).timestamp())

df = pd.read_csv('13/bitstampUSD_1-min_data_2012-01-01_to_2021-03-31.csv')
df.dropna(inplace=True)
del df['High'], df['Low'], df['Close'], df['Volume_(BTC)'], df['Volume_(Currency)'], df['Weighted_Price']
df = df[df['Timestamp'] > 1617144180]
print(len(df))
plt.plot(df['Timestamp'], df['Open'], '--')
plt.grid(axis='x')
plt.show()
