import pandas as pd

def compute_sem(df, column_name):
    # Excluding missing values
    df = df.dropna(subset=[column_name])

    # Compute standard error of the mean of groups
    sem = df.groupby(column_name)[column_name].sem()

    return sem

# Example usage
data = {
    'group': ['A', 'A', 'B', 'B', 'B', 'A', 'A'],
    'value': [1, 2, 2, 4, None, 1, None]
}

df = pd.DataFrame(data)

sem_result = compute_sem(df, 'group')
print(sem_result)
