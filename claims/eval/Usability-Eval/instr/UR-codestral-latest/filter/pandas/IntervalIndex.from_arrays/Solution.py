# Importing the pandas library
import pandas as pd

# Creating the arrays
left_bounds = [5, 10, 15, 20]
right_bounds = [15, 20, 25, 30]

# Creating the DataFrame with two columns
df = pd.DataFrame({'Left': left_bounds, 'Right': right_bounds}, index=[i for i in range(len(left_bounds))])

# Displaying the DataFrame
df
