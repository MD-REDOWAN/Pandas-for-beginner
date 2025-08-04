
# Scatter Plot

import pandas as pd
import matplotlib.pyplot as plt

x = pd.read_csv('games.csv')

x.plot(kind = 'scatter', x = 'turns', y = 'white_rating')

plt.show()
