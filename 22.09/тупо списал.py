import numpy as np
import matplotlib.pyplot as plt


x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])

A = np.vstack([x, np.ones(len(x))]).T
m, c = np.linalg.lstsq(A, y, rcond=None)[0]

plt.plot(x, y, 'o', label='Данные', markersize=10)
plt.plot(x, m * x + c, 'r', label='Аппроксимация')
plt.legend()
plt.show()
