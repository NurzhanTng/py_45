import matplotlib.pyplot as plt
import numpy as np

"""--- 1 туры ---"""
# x = [1, 2, 3, 4, 5]
# y = [2, 4, 6, 8, 10]

'''--- 2 туры ---'''
# y = 2 * x
def function(x):
    return np.sin(x)

# X = list(range(-100, 100))
X = [x/10 for x in range(-100, 100)]
Y = [function(x) for x in X]

"""--- 3 туры ---"""

X2 = np.linspace(-10, 10, 100)
Y2 = np.zeros(100)
for ind, x in enumerate(X2):
    Y2[ind] = function(x)


plt.plot(X2, Y2)

plt.title('График функции y = sinx')
plt.xlabel('Ось х')
plt.ylabel('Ось у')

plt.legend(['Геометрический график'], loc='upper left')
plt.show()