import pandas as pd
from io import StringIO

# Let's create a sample DataFrame for this example
data = {'Col1': [1, 2, 3], 'Col2': ['A', 'B', 'C']}
df = pd.DataFrame(data)

# To write Styler to a file as LaTeX format
# we first convert styled DataFrame to a LaTeX format
latex = df.style.to_latex()

# then we write it to a file
with open('output.tex', 'w') as tf:
    tf.write(latex)
