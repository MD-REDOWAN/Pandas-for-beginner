
# Read CSV Files (comma separated files) dataset

import pandas as pd

x = pd.read_csv('games.csv')

print(x)



print('------------------------')

# show the head the columns

print(x.head())


print("--------------------------------")

# There has any null true or false

print(x.null())

print('--------------------------')

print(x.isnull().sum())
# max_rows (The number of rows returned )

print("-------------------------")

print(pd.options.display.max_rows)

print("---------------------------")

print(x.shape)
