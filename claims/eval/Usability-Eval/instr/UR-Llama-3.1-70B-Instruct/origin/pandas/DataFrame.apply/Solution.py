# Import pandas library
import pandas as pd

# Create a sample DataFrame
data = {
    "Name": ["John", "Anna", "Peter", "Linda"],
    "Age": [28, 24, 35, 32],
    "Country": ["USA", "UK", "Australia", "Germany"]
}
df = pd.DataFrame(data)

# Define a function to calculate the length of a string
def calculate_length(x):
    return len(x)

# Apply the function along the axis of the DataFrame (in this case, we're applying it to each value in the 'Name' column)
df['Name_Length'] = df['Name'].apply(calculate_length)

# Print the resulting DataFrame
print(df)

# Alternatively, if you want to apply a function to the entire DataFrame (e.g., to calculate the mean age)
def calculate_mean_age(group):
    return group['Age'].mean()

df['Mean_Age'] = df.apply(calculate_mean_age, axis=1)

# Print the resulting DataFrame
print(df)

# However since apply function with axis=1 argument can also be implemented with help of np.vectorize function
import numpy as np

# Function to add 10 with the passed number
def add_ten(x):
    return x + 10

# Create a vectorized function
v_add_ten = np.vectorize(add_ten)

# Apply this operation to Values column in df
df['Age_new'] = v_add_ten(df['Age'])

# Print the resulting DataFrame
print(df)

# Also you can use 'applymap' along with a lambda function.
# This function takes a single DataFrame argument and returns a DataFrame with transformed values.

# Assume we have an array of values that need square calculation
df_squared = df[['Age']].applymap(lambda x: x**2)

# Print the resulting DataFrame
print(df_squared)
