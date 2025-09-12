import pandas as pd
from pdftk import pdfkit

# Assuming df is your DataFrame and 'style' is the style you want to apply
df.styler.to_latex('style.tex', index=False)

# If you want to write the style to a file
with open('style.tex', 'w') as f:
    f.write(df.styler.to_latex(index=False))

# If you want to write the style to a buffer
buffer = io.StringIO()
df.styler.to_latex(index=False, buf=buffer)
buffer_str = buffer.getvalue()

# If you want to write the style to a string
string_str = df.styler.to_latex(index=False)
