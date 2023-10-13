import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


fig = plt.figure(figsize = (16,9))
ax1 = fig.add_subplot(111) 

x_measured = [0.3112,
0.2882,
0.2802,
0.2752,
0.3182,
0.337879677,
0.320188929,
0.315269009,
0.31034909]
y_measured = [30.69,
29.8,
29.53,
29.44,
31.5,
30.58,
30.26,
30.1,
29.91
]
x_measured.sort ()
y_measured.sort ()

x = [0.27, 0.34]
y = np.interp(x, x_measured, y_measured)


ax1.scatter(x_measured, y_measured, marker='*')


ax1.errorbar(x_measured, y_measured, yerr=0.1, xerr = 0.001, color = 'k', linestyle = 'None')


ax1.plot(x,y, 'g')

ax1.grid() 

plt.show()
