import pandas as pd

# Create some example data
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35], 'Score': [88, 92, 85]}
df = pd.DataFrame(data)

# Use Styler to render the DataFrame as a LaTeX document
styler = df.style.to_latex()

# Writing the LaTeX output to a file
with open('output.tex', 'w') as f:
    f.write(styler)
