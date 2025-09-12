import pandas as pd

# Assuming a list of elements
elements = [1, 2, 3, '', False, 5, 6]

# Converting the list to a pandas series
elements_series = pd.Series(elements)

# Checking if all elements are truthy
if (elements_series.notnull().all()):
    print("All elements are truthy")
else:
    print("There are non-truthy elements")
