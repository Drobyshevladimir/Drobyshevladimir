import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig = plt.figure(figsize = (16,9))

ax1 = fig.add_subplot (221)
ax2 = fig.add_subplot (222)
ax3 = fig.add_subplot (223)
ax4 = fig.add_subplot (224)

values = np.random.normal(0, 10, 100)
ax1.hist(values, 50)
ax1.grid()


values = np.random.normal(0, 10, 1000)
ax2.hist(values, 50)
ax2.grid()


values = np.random.normal(0, 10, 10000)
ax3.hist(values,50)
ax3.grid()

values = np.random.normal(0, 10, 100000)
ax4.hist(values,50)
ax4.grid()

fig.show()
