import pandas as pd

# given string
string = 'one,two,three,four,five'

# given separator
sep = ','

# split the string by separator
series = pd.Series(string.split(sep))

# print the series
print(series)
