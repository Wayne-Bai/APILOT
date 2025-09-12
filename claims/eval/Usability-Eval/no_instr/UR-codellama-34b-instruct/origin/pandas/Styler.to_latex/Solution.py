
import pandas as pd

# create a sample dataframe
df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})

# create a Styler object from the dataframe
styler = df.style

# set the table name and caption for the LaTeX file
styler.set_table_name('my_table')
styler.set_caption("My Table Caption")

# write the DataFrame to a LaTeX file
with open('my_latex_file.tex', 'w') as f:
    styler.to_latex(f)
