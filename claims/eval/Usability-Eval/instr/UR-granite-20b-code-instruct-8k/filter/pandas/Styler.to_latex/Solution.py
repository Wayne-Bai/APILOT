
import pandas as pd

# Create a sample dataframe
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

# Create a Styler object
styler = df.style

# Generate LaTeX format
latex_format = styler.to_latex()

# Write to file
with open('output.tex', 'w') as file:
    file.write(latex_format)
