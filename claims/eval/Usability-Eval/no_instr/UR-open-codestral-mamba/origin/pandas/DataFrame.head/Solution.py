import pandas as pd

def first_n_rows(df, n):
    return df.head(n)

# usage
# assuming df is your pandas dataframe
# n is the number of rows you want to retrieve
# df = pd.read_csv('your_file.csv') # uncomment if you want to read data from a csv file
# n = 5 # replace with the number of rows you want to retrieve

# first_n_rows(df, n)
