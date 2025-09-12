import pandas as pd

# Assuming df is your DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [2, 4, 5, 4, 5],
    'C': [5, 5, 4, 4, 3],
    'D': [2, 2, 2, np.nan, 1]
})

# Function to compute pairwise correlation
def compute_correlation(df):
    # Compute pairwise correlation of columns, excluding NA/null values
    correlation = df.corr()
    return correlation

# Calculate and print correlation matrix
correlation_matrix = compute_correlation(df)
print(correlation_matrix)
