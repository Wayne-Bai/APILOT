import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}
df = pd.DataFrame(data)

# Apply styling
styled_df = df.style.set_table_attributes('style="display:inline"').highlight_max(axis=0)

# Save the styled DataFrame to an HTML file
with open('styled_dataframe.html', 'w') as f:
    f.write(styled_df.render())
