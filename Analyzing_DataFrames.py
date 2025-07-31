

# One of the most used method for getting a quick overview of the DataFrame, is the head() method.
# head(10) mean 10 rows but head() defult show 5 row

import pandas as pd

x = pd.read_csv('games.csv')

print(x)

print() # for space and separate

print(x.head(10))


print()

# There is also a tail() method for viewing the last rows of the DataFrame.
 
print(x.tail())


print()


# A method called info(), that gives you more information about the data set rows and columns object.

print(x.info())


print()


