import matplotlib.pyplot as plt
import numpy as np
from random import random


X = [x/10 for x in range(-100, 100)]
Y = [random() * x for x in X]

plt.plot(X, np.zeros(200), label='Граница x=0')
plt.plot(X, X, label='Граница y=x')
plt.scatter(X, Y, label='Распределение какой-то функции')
plt.legend()
plt.show()