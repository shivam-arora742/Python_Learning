# Aggregriate / GroupBy Statistics:

import pandas as pd

df=pd.read_csv('D:\Python_Learning\Pandas\modified_pokemon_data.csv')

print(df)

# Grouping data on basis of Type 1:
print(df.groupby('Type 1').mean())

# for sorted list:
print(df.groupby('Type 1').mean().sort_values('Attack',ascending=True))

# for summation of data of each type:
print(df.groupby('Type 1').sum())

# For counting records of each type:
print(df.groupby('Type 1').count())

# For multiple groups:
print(df.groupby(['Type 1','Type 2']).sum())

