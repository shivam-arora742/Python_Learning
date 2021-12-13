# Filtering Data using Pandas:

import pandas as pd

df=pd.read_csv('D:\Python_Learning\Pandas\modified_pokemon_data.csv')



# Get data based on single condition:
print(df.loc[df['Attack']==49])

# Get data based on multiple conditions: (using & operator)
print(df.loc[(df['Attack']== 49) & (df['Type 1']=='Water')])

#using Arithmetic Conditions for Filtering Data:
print(df.loc[(df['Attack']== 49) & (df['Type 1']=='Water') & (df['Defense']>100)])

# Get data based on multiple conditions: (using | operator)
# print(df.loc[(df['Attack']==49) | (df['Type 1']=='Water')])

# Reset Index for Filtered Data:
new_df=df.loc[(df['Attack']== 49) | (df['Type 1']=='Water')].reset_index()
print(new_df)

# ------------------------------------------------------------------------------------------------

# Regex Filtering:

# FIltered out data having 'Mega' in Name:
print(df.loc[df['Name'].str.contains('Mega')])

# # FIltered out data not having 'Mega' in Name:
print(df.loc[~df['Name'].str.contains('Mega')])

# Filtering using regex:(filtering data having type-1 as fire or grass):-
import re
print(df.loc[df['Type 1'].str.contains('Fire|Grass',regex=True)])