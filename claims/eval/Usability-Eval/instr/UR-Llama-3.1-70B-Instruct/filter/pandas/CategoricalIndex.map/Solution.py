# Import pandas library
import pandas as pd
import numpy as np

# Create a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Dave', 'Emily'],
    'Age': [25, 30, 35, 40, 45],
    'Country': ['USA', 'Canada', 'Mexico', 'UK', 'Australia']
}
df = pd.DataFrame(data)

# Function that we want to map
def square(x):
    return x ** 2

# Mapping the 'Age' column using the function
df['Age_Squared'] = df['Age'].transform(square)

print("Mapped DataFrame:\n", df)

# Create a mapping dictionary
country_map = {
    'USA': 'United States',
    'Canada': 'CA',
    'Mexico': 'MX',
    'UK': 'United Kingdom',
    'Australia': 'AU'
}

# Map values in the 'Country' column using the dictionary
df['Country_Full'] = df['Country'].transform(lambda x: country_map.get(x))

print("\nMapped DataFrame with country names:\n", df)
