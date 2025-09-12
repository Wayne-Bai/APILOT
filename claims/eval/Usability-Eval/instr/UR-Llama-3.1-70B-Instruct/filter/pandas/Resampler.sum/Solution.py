import pandas as pd

# Create a sample DataFrame
data = {
    'Group': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Values': [10, 20, 30, 40, 50, 60]
}
df = pd.DataFrame(data)

# Compute sum of group values
group_sums = df.groupby('Group')['Values'].aggregate(pd.Series.aggregate)

# Alternatively, using the agg function for more flexibility
group_sums_agg = df.groupby('Group')['Values'].agg(lambda x: pd.Series.aggregate(x))

# Using the apply function for custom aggregations
def custom_sum(x):
    return x.values.sum()
group_sums_apply = df.groupby('Group')['Values'].apply(custom_sum)

print("Group Sums (aggregate):")
print(group_sums)
print("\nGroup Sums (agg):")
print(group_sums_agg)
print("\nGroup Sums (apply):")
print(group_sums_apply)
