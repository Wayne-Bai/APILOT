import pandas as pd

# Create a sample DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})

# Create a Styler object
styler = df.style.format({
    'A': '{:.2f}',
    'B': '{:.1f}',
    'C': '{:.0f}'
})

# Write the Styler to a LaTeX file
styler.to_latex('styler.tex')

# The above code will write the Styler to a file named 'styler.tex' in the current directory
# You can also write it to a buffer or string using the 'buffer' or 'string' parameters respectively

# Note: The 'to_latex' method is an outdated API and it is recommended to use the 'to_latex' method from pandas.io.formats.latex module instead.
