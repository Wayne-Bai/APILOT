import pandas as pd
from pandas.io.formats.format import Styler

# Assuming df is your DataFrame
df = pd.DataFrame(...)

# Create a Styler object
styler = df.style

# Write Styler to a LaTeX formatted string
latex_string = styler.render().to_latex(index=False)

# Print the LaTeX formatted string
print(latex_string)
