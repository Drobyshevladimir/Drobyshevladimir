import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


fig = plt.figure(figsize = (16,9)) # создали рисунок/Figure Fig пропорциями 16:9
ax1 = fig.add_subplot(111) # допустим, больше 1 графика нам не надо

x_measured = [1.01, 2.59, 3.03, 5.40, 7.33]
y_measured = [0.41, 0.84, 1.11, 3.22, 5.00]

#используем встроенный линейный интерполятор чтобы посчитать значения прямой МНК в точках, на которых будем строить нашу прямую
#Поскольку мы хотим прямую, нам достаточно двух точек -- начало и конец прямой
x = [0.5, 9.0]
y = np.interp(x, x_measured, y_measured)

# ставим точки функцией scatter, точки будем ставить крестиком
ax1.scatter(x_measured, y_measured, marker='x')

# поставим кресты погрешностей, linestyle = None, чтобы кресты не соединялись прямыми
ax1.errorbar(x_measured, y_measured, yerr=0.2, xerr = 0.1, color = 'm', linestyle = 'None')

#построим красную прямую МНК
ax1.plot(x,y, 'r')

ax1.grid() # делаем сетку

# для готового графика для лабы по общефизу не хватает только названия, подписанных осей и легенды, но это вы уже умеете
# успехов!
fig.show()
