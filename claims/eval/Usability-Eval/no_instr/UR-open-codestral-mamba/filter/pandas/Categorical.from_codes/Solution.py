import pandas as pd

# Creating a series with codes and categories
codes = [1, 2, 3, 2, 2, 1, 3, 1]
categories = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Holiday"]
series = pd.Series(codes, categories=categories)

# Converting the series to categorical type
series = series.astype("category")

series
