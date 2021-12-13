# Sorting/ Descibing Data:

import pandas as pd

df=pd.read_csv('D:\Python_Learning\Pandas\pokemon_data.csv')

print(df)

# Get info about mean,min,max & etc about data:
print(df.describe())


# Sorting of data :(ascending order)
print(df.sort_values('Name'))

# # Sorting of data :(descending order)
print(df.sort_values('Name',ascending=False))


# Sorting multiple values:
print(df.sort_values(['Type 1','HP'],ascending=[1,0])) 

# 0-for false:
# 1-for true: 