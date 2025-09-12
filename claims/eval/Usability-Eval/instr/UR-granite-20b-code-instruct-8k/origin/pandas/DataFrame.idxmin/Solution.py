import pandas as pd
data = pd.DataFrame({'A': [4, 2, 1, 3, 5], 'B': [20, 10, 15, 17, 25]})
index_of_min = data.idxmin()
print(index_of_min)
