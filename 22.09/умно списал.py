import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
fig = plt.figure(figsize = (16,9))
ax1 = fig.add_subplot(111) 




x=[2, 5, 6, 8, 9]
y=[3, 4, 9, 10, 12]
x0=[0,max(x)]
y0=np.interp(x0, x, y)
print('y=',y0[1]/x0[1],'*x+',y0[0])


ax1.plot(x0,y0, 'g')

ax1.scatter(x, y, marker='*')
ax1.grid() 

plt.show()
