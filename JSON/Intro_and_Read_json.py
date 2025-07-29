
# Big data sets ate often stored, or extracted as json

# JSON is plain text, but has the format of an object, and is well known in the world of programming, including Pandas.
# In our examples we will be using a JSON file called 'data.json'.

import pandas as pd

data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}

x = pd.DataFrame(data)

print(x) 



# JSON is a syntax for storing and exchanging data.

# JSON is text, written with JavaScript object notation.



print('-------------------------------')


import json

a =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(a)

# the result is a Python dictionary:
print(y["age"])



print('-----------------------')


import pandas as pd

z = pd.read_json('game.json') # file not available .Output show error

print(z.to_string())
