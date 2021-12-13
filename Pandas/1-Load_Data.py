# Loading Data into Pandas:

# import pandas:
import pandas as pd

# # load data from CSV to Pandas:
df=pd.read_csv('D:\Python_Learning\Pandas\pokemon_data.csv')

# print full loaded data:
print(df)

# print few rows from top:
print(df.head(4))

# print few rows from bottom:
print(df.tail(4))



# # Load data from Excel file:
df_xlsx=pd.read_excel('D:\Python_Learning\Pandas\pokemon_data.xlsx')
print(df_xlsx)
print(df_xlsx.head(3))



# Load data from Text file:
# load whole txt data into single column:
df_txt = pd.read_csv('D:\Python_Learning\Pandas\pokemon_data.txt')

# Load txt data in seperate columns:
df_txt = pd.read_csv('D:\Python_Learning\Pandas\pokemon_data.txt',delimiter='\t')

print(df_txt)
