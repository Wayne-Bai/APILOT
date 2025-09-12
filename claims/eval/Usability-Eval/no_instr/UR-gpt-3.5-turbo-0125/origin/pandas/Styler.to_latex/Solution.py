
import pandas as pd

# Create a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'Salary': [50000, 60000, 70000, 80000]}

df = pd.DataFrame(data)

# Define a function to convert DataFrame to LaTeX format
def to_latex(df):
    return df.to_latex()

# Write the styled DataFrame to a file in LaTeX format
with open('styled_table.tex', 'w') as f:
    f.write(to_latex(df))
