import pandas as pd

# Assuming you have a dataframe 'df' with a column 'values' and a column 'group'
df = pd.DataFrame({'values': [1, 2, 3, 4, None, 6, 7, None, 9, 10],
                   'group': ['A', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'A']})

def sem_of_group(df, column, group):
    # Compute mean and number ofvalid values for each group
    grouped = df[[column, group]].dropna().groupby(group)
    mean = grouped[column].mean()
    count = grouped[column].count()

    # Compute standard deviation for each group
    std = grouped[column].std()

    # Compute Standard Error of Measurement (SEM) for each group
    sem = std / count**.5

    return sem

sem_of_group(df, 'values', 'group')
