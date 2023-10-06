import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# принцип настройки схожий, но вместо plt.plot используем plt.bar
labels = ['A', 'B', 'C']
values = [1,4,3]

plt.figure(figsize=(5,3), dpi=100)

bars = plt.bar(labels, values)

plt.savefig('barchart.png', dpi=300)

plt.show()
