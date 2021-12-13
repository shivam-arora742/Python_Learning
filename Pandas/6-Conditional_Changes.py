# Changing the data in the file based on conditions:

import pandas as pd

df=pd.read_csv('D:\Python_Learning\Pandas\modified_pokemon_data.csv')

print(df)

# Conditional Changes:

#  changing type 1 from grass to land:
df.loc[df['Type 1']=='Grass','Type 1']='Land'

# we can specify other column name as well:
df.loc[df['Type 1']=='Land','HP']='0'


# Multiple conditional changes at a time:
df.loc[df['Total']>400,['Generation','Legendary']]=['2','True']
print(df)