# Importing the pandas library
import pandas as pd

# Creating a sample DataFrame
data = {
    'Employee': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 24, 35, 32],
    'Salary': [50000, 60000, 70000, 80000]
}
df = pd.DataFrame(data)

# Printing the original DataFrame
print("Original DataFrame:")
print(df)

# Hide the entire index / column headers, or specific rows / columns from display
# Hide the index headers
pd.options.display.show_index = False
# Hide the 'Age' column
df = df.drop(columns=['Age'])

# Printing the modified DataFrame
print("\nDataFrame after hiding headers and 'Age' column:")
print(df)
