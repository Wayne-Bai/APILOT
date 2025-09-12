import pandas as pd

# Create a sample DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})

# Use the Styler to style the DataFrame
styled_df = df.style.applymap(lambda x: 'color: red;')

# Write the styled DataFrame to an HTML file
styled_df.to_html('styled_dataframe.html')
