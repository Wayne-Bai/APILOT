import pandas as pd

# Let's say we have a dataframe df with two columns 'group' and 'value'
df = pd.DataFrame({
    'group': ['A', 'B', 'A', 'B', 'B'],
    'value': [5, 10, 2, 4, 3]
})

# To compute the product of group values,
# we need to group the dataframe on 'group',
# and then apply a lambda function to calculate the product of 'values' within each group

df.groupby('group').apply(lambda x: x['value'].prod())
