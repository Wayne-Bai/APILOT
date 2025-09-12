import pandas as pd

# Sample DataFrame
data = {
    'Column1': [1, 2, 3],
    'Column2': [4, 5, 6]
}
df = pd.DataFrame(data)

# Applying styles to the DataFrame
styled_df = df.style.highlight_max(axis=0)

# Writing the Styler to a LaTeX file
styled_df.to_latex('styled_dataframe.tex', burn_header=False)
