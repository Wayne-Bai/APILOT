import pandas as pd

# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

# Create a Styler object
styler = df.style

# Output the Styler to LaTeX format
latex_str = styler.to_latex()

# Optionally, save the LaTeX output to a file
with open('output.tex', 'w') as f:
    f.write(latex_str)
