
# Pandas Series one-dimensional array holding datatype .It actually work as colums

import pandas as pd

Result = [90.5, 80, 70]

x = pd.Series(Result)

print(x)



print("----------------------------")


# Labels (index): This label can be used to access a specified value ,start from first value index 0, second value index 1

# Creat Lables

import pandas as pd

a = [3.92, 3.78, 3.50]

y = pd.Series(a, index= ['Nabil', 'Utsho', 'Ismail'])

print(y)

print(y["Nabil"]) # 3.92  just return y Nabil result



print("-------------------")

# key/ value object a sseries

import pandas as pd

dataset = {"Akib":24, "Ebnul": 22, "Limon": 32}

z= pd.Series(dataset)

print(z)


