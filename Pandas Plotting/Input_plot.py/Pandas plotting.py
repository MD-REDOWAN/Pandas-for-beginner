
# Pandas Ploting

import pandas as pd
import matplotlib.pyplot as plt

x = pd.read_csv('games.csv')
print(x)

x.plot()
plt.show()