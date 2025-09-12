import pandas as pd

# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 27, 22],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)

# Styler object
styler = df.style.format({'Age': '{:d}'})

# Convert Styler to LaTeX
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
