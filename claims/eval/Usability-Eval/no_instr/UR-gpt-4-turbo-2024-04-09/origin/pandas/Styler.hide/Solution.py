import pandas as pd

# Create a sample DataFrame
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}
df = pd.DataFrame(data)

# Hide the entire DataFrame index using display options
pd.options.display.show_index = False

# Display the DataFrame to check the effect of hiding
print(df, "\n")

# Reset index display option to default
pd.options.display.show_index = True

# Hide specific rows by slicing the DataFrame, here hiding the first row
print(df.iloc[1:], "\n")

# Hide specific columns by selecting columns, here hiding column 'A'
print(df[['B', 'C']])
