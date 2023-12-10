import numpy as np
import pandas as pd

dict1 = {
    "name" :['harry','john','steve'],
    "marks":[89,90,73],
    "city" : ['Delhi','Banglore','Kolkata']
}

# create a data frame
df = pd.Dataframe(dict1)

# when user don't want to access index excel sheet
df.to_csv('friends_indexfals.csv', index=false)

# to display starting 2 rows
print(df.head(2))

# to display last 2 rows
print(df.tail(2))

# statistical analysis of the data
print(df.describe)

# to display total number of elements present
print(df.size)

# to display max & min value of data
print(df.max)
print(df.min)

# to display mean & median value of data
print(df.mean())
print(df.median())

# to display sum of rows
print(df.sum(axis=1))

# to display sum of columns
print(df.sum(0))

# deleting a row
df = df.drop(1)
print(df)
print()

# deleting a column
df = df.drop(['Name'], axis=1)
print(df)

# series
Ser = pd.series(np.random.rand(34)
print(ser)

newdf = pd.dataframe(np.random.rand(234, 7), index=np.arange(234))
print(newdf.head)  # display starting 5 rows
print(newdf)  # give detail about data frame

newdf = newdf.dtypes  # dispaly datatypes of the given data
print(df)
newdf[0][0] = 'Harry'

print(newdf.index)  # display index of data till 234
print(newdf.to_numpy)  # to create numpy array
print(newdf.loc[1][1])  # Accessing values

Tp = newdf.t  # transpose
newdf.sort_index(axis=1, ascending=false)  # sorting data

# converting csv file into dataframe
df = pd.read_csv('new_sample.csv')
print(df)












