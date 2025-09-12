
import pandas as pd

# Consider the following example dataframe df
df = pd.DataFrame({
    'group':['A', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'B'],
    'values':[1, 2, 3, 4, 5, 6, 7, 8, 9]
})

# To calculate the product of the 'values' for each 'group'
product_of_values = df.groupby('group')['values'].prod()

print(product_of_values)
