import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


fig = plt.figure(figsize = (16,9)) 
ax1 = fig.add_subplot(111) 

df = pd.read_csv('iris_data.csv')

x1=[]
y1=[]
for i in range(150):
    x1.append(list(df['PetalWidthCm'])[i])
    y1.append(list(df['PetalLengthCm'])[i])

print((x1))
print((y1))
x_measured = [x1]
y_measured = [y1]

x_measured.sort ()
y_measured.sort ()
x = [0.0, 2.5]



y = np.interp(x, x_measured, y_measured)

ax1.scatter(x_measured, y_measured, marker='x')

ax1.plot(x,y, 'r')

ax1.grid() 

plt.show()
