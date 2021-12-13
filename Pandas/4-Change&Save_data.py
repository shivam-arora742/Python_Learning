# Making changes to Dataframe:

import pandas as pd

df=pd.read_csv('D:\Python_Learning\Pandas\pokemon_data.csv') 

print(df.head(10))

# Add new column by adding previous columns:
df['Total']=df['HP']+df['Attack']+df['Speed']
print(df.head(10))

# delete a specific columns:
df=df.drop(columns=['Total'])
print(df.head(10))

# Another way to add new columns:
df['Total']=df.iloc[:,4:10].sum(axis=1)
print(df.head(5))

# Rearrange Columns:
  # save columns name in list:
cols=list(df.columns.values)
  # now reorder the columns name:
df=df[cols[0:4]+[cols[12]]+cols[4:12]]   

print(df.head(5))

# ------------------------------------------------------------------------------------------------------------

# Saving data from Pandas to files:

print(df)

# Saving data to csv file:
# df.to_csv('modified_pokemon_data.csv')

# to avoid index column:
df.to_csv('modified_pokemon_data.csv',index=False)

# checking whthr file created or not:
# df_modified=pd.read_csv("D:\Python_Learning\modified_pokemon_data.csv")

# Saving data to excel:
df.to_excel('modified_pokemon_data.xlsx',index=False)

# Saving data to text file:
df.to_csv('modified_pokemon_data.txt',index=False,sep='\t')
# sep->seperator used to uniquely identify columns:




