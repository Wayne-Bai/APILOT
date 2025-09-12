import pandas as pd

# Sample DataFrame for demonstration
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'City': ['New York', 'Paris', 'Berlin', 'London'],
    'Salary': [70000, 85000, 60000, 95000]
}
df = pd.DataFrame(data)

# Defining a sample function that will be called on each value in the DataFrame
def my_function(value):
    return value * 0.9  # Example: decrease each value by 10%

# Applying the function to the DataFrame
df_aug = df.map(lambda x: my_function(x))

print(df_aug)
