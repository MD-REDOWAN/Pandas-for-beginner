
# For kind argument will be Kind = 'hist'



import pandas as pd
import matplotlib.pyplot as plt

x = pd.read_csv('games.csv')

x.plot(kind = 'hist', x = 'turns', y = 'white_rating')

plt.show()