
import pandas as pd

# Create a Pandas DataFrame with some sample data
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': ['apple', 'banana', 'orange']})

# Use the to_latex() method to convert the DataFrame to LaTeX format
df_latex = df.to_latex(index=False)

# Print the LaTeX code to the console
print(df_latex)
