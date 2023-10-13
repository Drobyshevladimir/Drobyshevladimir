import matplotlib.pyplot as plt
import numpy as np
import pandas as pd




fig = plt.figure()
plt1 = fig.add_subplot(121)
plt2 = fig.add_subplot(122)



df = pd.read_csv('iris_data.csv')
plt1.pie([(list(df['Species']).count('Iris-setosa')),list(df['Species']).count('Iris-versicolor'), list(df['Species']).count('Iris-virginica')], labels = ['Iris-setosa','Iris-versicolor','Iris-virginica'])
nummim=0
numaverage=0
nummax=0
for i in range(150):
    if list(df['PetalLengthCm'])[i]<1.2:
        nummim+=1
    elif list(df['PetalLengthCm'])[i]<1.5:
        numaverage+=1
    else:
        nummax+=1



plt2.pie([nummim,numaverage,nummax], labels = ['<1.2cm','1.2cm-1.5cm','>1.5cm'])
fig.show()
