import pandas as pd
from pandas.io.latex import Latex

# Assuming df is your DataFrame
latex_tabular = Latex.to_latex(df)

# Write to a file
with open('output.tex', 'w') as f:
    f.write(latex_tabular)

# Or write to a buffer or string
buffer = io.StringIO()
buffer.write(latex_tabular)

# Or write to a string
latex_tabular_string = Latex.to_latex(df, buffer=True)
