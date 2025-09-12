# Import pandas library
import pandas as pd

# Create a simple DataFrame
data = {
    'Name': ['Amy', 'Jack', 'Lucy', 'Jake', 'John'],
    'Grade': ['A', 'B', 'A', 'C', 'B']
}

df = pd.DataFrame(data)

# Print original DataFrame
print("Original DataFrame:")
print(df)

# Define a function to map grades to points
def map_grade_to_points(grade):
    if grade == 'A':
        return 5
    elif grade == 'B':
        return 4
    elif grade == 'C':
        return 3
    else:
        return 0

# Use the map function to apply the mapping
df['Points'] = df['Grade'].apply(map_grade_to_points)

# Print DataFrame after mapping
print("\nDataFrame after mapping:")
print(df)

# Alternatively, you can use a dictionary to map values
grade_to_points_map = {'A': 5, 'B': 4, 'C': 3}

# Use the map function to apply the mapping
df['Points'] = df['Grade'].map(grade_to_points_map).fillna(0)

# Print DataFrame after mapping
print("\nDataFrame after mapping with a dictionary:")
print(df)
