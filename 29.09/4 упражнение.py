import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


fig = plt.figure(figsize = (16,9)) # создали рисунок/Figure Fig пропорциями 16:9
ax1 = fig.add_subplot(111) 

df = pd.read_csv('iris_data.csv')
'''green1=[]
green2=[]
yellow1=[]
yellow2=[]
blue1=[]
blue2=[]
'''
x_measured = [list(df['PetalLengthCm'])]
y_measured = [list(df['SepalLengthCm'])]



ax1.scatter(x_measured, y_measured, marker='x')


fig.show()
