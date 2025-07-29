
# First step Installation of Pandas

# We need to install python and PIP 

# Using : 'C:\Users\Your Name>pip install pandas' command

# Checking Pandas Version import pandas as pd

import pandas
print(pandas.__version__) # 2.3.1



# Import Pandas

import pandas

data = {

    'student' : ['Akib', 'Ebnul', 'Limon'],
    'Result' : [90, 80, 70]
}


x = pandas.DataFrame(data)
print(x)


# just print for easy to understand the separate Output:
print("---------------------------")

# Pandas usually imported under the pd 


import pandas as pd

data2 = {
    "student" : ["Shihab", "Aheen", "Jeba"],
    "Result" : [100, 80, 90]
}


y = pd.DataFrame(data2)
print(y)


