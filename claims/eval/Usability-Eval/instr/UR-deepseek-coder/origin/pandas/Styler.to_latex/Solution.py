import pandas as pd

# Sample DataFrame
data = {
    'Column1': [1, 2, 3],
    'Column2': [4, 5, 6]
}
df = pd.DataFrame(data)

# Create a Styler object
styler = df.style

# Apply some styles (optional)
styler.highlight_max(color='yellow')

# Convert Styler to LaTeX format
latex_output = styler.to_latex()

# Write to a file
with open('output.tex', 'w') as f:
    f.write(latex_output)

# Write to a buffer (StringIO)
from io import StringIO
buffer = StringIO()
buffer.write(latex_output)

# Get the string from the buffer
latex_string = buffer.getvalue()

# Print the LaTeX string
print(latex_string)
