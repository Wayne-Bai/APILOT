import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
}
df = pd.DataFrame(data)

# Styling the DataFrame
styled_df = df.style.highlight_max(color='lightgreen').highlight_min(color='lightcoral')

# Writing the styled DataFrame to an HTML file
styled_df.to_html('styled_dataframe.html')
