
# DataFrame : usually muti dimensional table like column, rows that's mean the whole table

import pandas as pd

student_category= {

    "Name" : ["Raju", "Aysha", "Jeba"],
    "Category": ["CR", "student","CR"]
}


x = pd.DataFrame(student_category)

print(x)


print("----------------------")

# Locate Row (loc attribute to return one or more specified row)

print(x.loc[1])

# show the 1 number index row

print("----------------------")

# Named Row Indexes define like year

y = pd.DataFrame(student_category,index= ["year1","year2","year3"])
print(y)


print("----------------------")
# Locate Named Indexes

print(y.loc["year2"])


