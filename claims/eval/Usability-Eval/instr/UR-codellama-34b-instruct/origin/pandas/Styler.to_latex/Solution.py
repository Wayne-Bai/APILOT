import pandas as pd
from io import StringIO

# create a sample dataframe
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 40, 30],
        'Gender': ['Female', 'Male', 'Non-binary']}
df = pd.DataFrame(data)

# convert the dataframe to LaTeX format
buf = StringIO()
df.to_latex(buf=buf)
latex_str = buf.getvalue()

# write the LaTeX string to a file or buffer
with open('output.tex', 'w') as f:
    f.write(latex_str)
