import pandas as pd

# Create a sample DataFrame for demonstration
data = {'A': [1, 2, 3, 4, 5],
        'B': [5, 4, 3, 2, 1],
        'C': [10, 9, 8, 7, 6]}

df = pd.DataFrame(data)

# Calculate the quantile for each column at 0.5 (median) quantile
quantile_values = df.quantile(0.5)

# Print the quantile values
print(quantile_values)
