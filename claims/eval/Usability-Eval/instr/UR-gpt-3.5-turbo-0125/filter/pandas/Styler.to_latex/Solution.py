
import pandas as pd

df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})

styler = df.style.set_caption('My Styled DataFrame')
latex = styler.to_latex()

# Write LaTeX formatted Styler to a file
with open('styled_dataframe.tex', 'w') as f:
    f.write(latex)

# Write LaTeX formatted Styler to a buffer
buffer = io.StringIO()
buffer.write(latex)
buffer.seek(0)

# Write LaTeX formatted Styler to a string
latex_str = styler.render()
