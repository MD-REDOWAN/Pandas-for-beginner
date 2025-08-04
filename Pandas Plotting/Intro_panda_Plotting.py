
# pandas uses the plot() method to create diagrams

import sys
import matplotlib
matplotlib.use("Agg")


import pandas as pd

import matplotlib.pyplot as plt

x = pd.read_csv('game.csv')

x.plot()
plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()