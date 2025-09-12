import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6]
}
df = pd.DataFrame(data)

# Applying some styling to the DataFrame
styled_df = df.style.highlight_max(axis=0)

# Save the styled DataFrame to a LaTeX file
with open('styled_table.tex', 'w') as f:
    f.write(styled_df.to_latex())
