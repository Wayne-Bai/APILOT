from pandas import DataFrame

# Sample data
data = {
    'A': [1, 2],
    'B': [3, 4]
}

index = ['Level_1', 'Level_1']

df = DataFrame(data, index=index)
print(df)