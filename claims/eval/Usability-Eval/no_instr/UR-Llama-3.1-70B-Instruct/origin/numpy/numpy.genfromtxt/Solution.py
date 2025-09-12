import numpy as np

# Define the path to the text file
file_path = 'data.txt'

# Load data from the text file, with missing values handled as specified
# Here, we use genfromtxt function to load the data
# The'missing_values' parameter is used to define the representation of missing values
# The 'filling_values' parameter is used to replace the missing values with a specific value
data = np.genfromtxt(file_path, 
                     dtype=None, 
                     encoding=None, 
                     names=True, 
                     excludelist=None, 
                     deletechars=None, 
                     replace_space='_', 
                     autostrip=False, 
                     skip_header=0, 
                     skip_footer=0, 
                     usecols=None, 
                     unpack=False, 
                     loose=False, 
                     invalid_raise=True, 
                     max_rows=None, 
                     max_cols=None, 
                     missing_values='NaN',
                     filling_values=np.nan, 
                     usemask=False)

print(data)
