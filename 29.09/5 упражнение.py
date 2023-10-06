import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


fig = plt.figure(figsize = (16,9)) 
ax1 = fig.add_subplot(111) 
N=[]
df = pd.read_csv('BTC_data.csv')
for i in range(1457):
    N.append(i)
x_measured = [N]
y_measured = [list(df['close'])]

ax1.scatter(x_measured, y_measured, marker='x')

ax1.grid() 

plt.show()
