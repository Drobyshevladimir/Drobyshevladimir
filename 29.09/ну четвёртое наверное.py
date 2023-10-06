import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# попробуем сгенерировать случайные числа из нормального распределения и посмотреть, как оно выглядит

# среднее
pos = 0
 
# параметр отвечающий за разброс
scale = 10
 
# размер массива случайных чисел (сколько их сгенерируем)
size = 10000000
 
# используем функцию из подраздела random библиотеки numpy и передадим наши параметры
values = np.random.normal(pos, scale, size)
 
# строим гистограмму с 100 блоков
plt.hist(values, 100)

plt.show()
