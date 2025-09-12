import pandas as pd

# Creating a multi-index dataframe
data = {
    'level1_index1': {
        ('index2_1', 'features1'): 1,
        ('index2_1', 'features2'): 2,
        ('index2_2', 'features1'): 3,
        ('index2_2', 'features2'): 4
    },
    'level2_index1': {
        ('index2_1', 'features1'): 5,
        ('index2_1', 'features2'): 6,
        ('index2_2', 'features1'): 7,
        ('index2_2', 'features2'): 8
    }
}

# Making the data a multi-index dataframe
multi_index = pd.MultiIndex.from_tuples(
    [('index2_1', 'features1'), ('index2_1', 'features2'),
     ('index2_2', 'features1'), ('index2_2', 'features2')],
    names=["index2", "features"]
)

df = pd.DataFrame(data, index=[('level1_index1', 'values'), ('level2_index1', 'values')])
df['level1_index1'] = df['level1_index1'].rename_axis('index2', axis="columns")
df['level2_index1'] = df['level2_index1'].rename_axis('index2', axis="columns")
df = df.T.reset_index()
print(df)
