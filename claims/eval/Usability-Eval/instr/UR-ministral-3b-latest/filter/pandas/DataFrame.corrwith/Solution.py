import pandas as pd

# Assuming that you have a DataFrame named df
# df = pd.read_csv('your_data.csv')

# To compute pairwise correlation
correlation_matrix = df.corr(method='pearson')
print(correlation_matrix)
