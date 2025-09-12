import pandas as pd

# create a sample DataFrame
data = {'A': [1, 2, 3, 4, 5], 'B': [6, 7, 8, 9, 10]}
df = pd.DataFrame(data)

# calculate the index of the first occurrence of the maximum value over a given axis
first_occurence_idx = df['A'].idxmax()
print(first_occurence_idx) # output: 3
