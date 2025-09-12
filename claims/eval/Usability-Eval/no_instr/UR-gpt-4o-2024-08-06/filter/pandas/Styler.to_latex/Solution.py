import pandas as pd

# Sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 27, 22],
    'Salary': [50000, 48000, 55000]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a Styler object
styler = df.style

# Optionally, you can style the DataFrame
# Example: Highlight Max
styler = styler.highlight_max(subset=['Age', 'Salary'], color='lightgreen')

# Write the Styler to a LaTeX file
latex_output = styler.to_latex()

# Save the LaTeX output to a file
with open('dataframe.tex', 'w') as f:
    f.write(latex_output)
