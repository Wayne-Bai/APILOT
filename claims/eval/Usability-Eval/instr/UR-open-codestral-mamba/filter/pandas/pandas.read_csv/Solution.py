# Importing pandas library
import pandas as pd

# Using pandas read_csv function to read a csv file into a DataFrame
df = pd.read_csv('file.csv')

#To handle large csv file in chunks use:
chunksize = 10 ** 6
for chunk in pd.read_csv("file.csv", chunksize=chunksize):
    process(chunk) #Replaced with your processing function
