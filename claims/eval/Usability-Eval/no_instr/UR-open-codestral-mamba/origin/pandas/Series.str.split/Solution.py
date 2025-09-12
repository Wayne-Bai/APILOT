import pandas as pd

# Suppose our strings and separator are defined as follows:

strings = ["apple,orange,banana", "car,motorbike,truck", "dog,cat,rat"]
separator = ","

# We can use pandas' `str.split()` function to create a list of lists containing each string split around the separator.

split_strings = [s.split(separator) for s in strings]

# Now, let's create a pandas DataFrame from this list of lists:

df = pd.DataFrame(split_strings)

print(df)
