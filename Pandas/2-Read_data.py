# Reading data into Pandas:

import pandas as pd

df=pd.read_csv('D:\Python_Learning\Pandas\pokemon_data.csv')

# Read Column Headers:
print(df.columns)

# Read Specific Column:
print(df['Name'])
# for multiple cols:
print(df[['Name','Type 1']])


# Read data from Specific Rows:
print(df.iloc[3])
print(df.iloc[1:4])

# Read from Specific Location: (Row,Col):
print(df.iloc[795,3])

# # Iterate through each row:
for index, row in df.iterrows():
    print(index,row)


# Getting row data based on condition:
print(df.loc[df['Attack']==62])