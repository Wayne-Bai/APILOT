
import pandas as pd

# create a sample dataframe for demonstration purposes
data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
df = pd.DataFrame(data)

# compute the product of each group using the groupby function
prod_df = df.groupby(['A', 'B']).agg({'C': 'prod'})
print(prod_df)
