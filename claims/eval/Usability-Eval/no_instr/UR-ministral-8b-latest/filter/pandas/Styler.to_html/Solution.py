import pandas as pd

# Sample data
data = {'column1': [1, 2, 3], 'column2': ['A', 'B', 'C']}
df = pd.DataFrame(data)

# Apply styling to the DataFrame
styled_df = df.style.set_properties(**{'background-color': 'lightgrey'})

# Save the styled DataFrame as HTML
styled_df.to_html('styled_table.html', index=False)
