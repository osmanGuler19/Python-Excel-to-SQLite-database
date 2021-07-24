import pandas as pd
import sqlite3
import csv
#Excel to CSV
read_file = pd.read_excel (r'example.xlsx',engine='openpyxl')
read_file.to_csv (r'output.csv', index = None, header=True)

#CSV editing
##You can do anything with csv file. It is very easy with pandas 
df = pd.read_csv('output.csv')
df.drop(df.columns[0], axis=1, inplace=True)
df.to_csv('output.csv')
cols = len(df.axes[1])
print("Number of Columns: ", cols)
myselectlist = ['Productcode', 'Product_omschrijving','ENERCC_kcal', 'PROT_g','SUGAR_g','FAT_g']
selectlist = [x for x in df.columns if x in myselectlist]
df.loc[:,selectlist].to_csv('new.csv')

####CSV to SQLite Database
# Connect to SQLite database
conn = sqlite3.connect('data.db')

# Load CSV data into Pandas DataFrame
stud_data = pd.read_csv('new.csv')
# Write the data to a sqlite table
stud_data.to_sql('ingredients', conn, if_exists='replace', index=False)

# Create a cursor object
cursor = conn.execute('select * from ingredients')
names = [description[0] for description in cursor.description]
print(names)
# Fetch and display result
for row in cursor.execute('SELECT * FROM ingredients'):
    print(row)
# Close connection to SQLite database
conn.close()

