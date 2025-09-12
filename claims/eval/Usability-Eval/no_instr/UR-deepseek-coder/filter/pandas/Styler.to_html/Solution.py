import pandas as pd

# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 27, 22],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)

# Apply some styling to the DataFrame
styled_df = df.style.set_table_styles([
    {'selector': 'th', 'props': [('background-color', 'yellow'), ('color', 'black')]},
    {'selector': 'td', 'props': [('border', '1px solid black')]}
])

# Write the styled DataFrame to an HTML file
with open('styled_table.html', 'w') as f:
    f.write(styled_df.to_html())

# Write the styled DataFrame to a string
html_string = styled_df.to_html()

# Write the styled DataFrame to a buffer (BytesIO)
import io
buffer = io.StringIO()
styled_df.to_html(buf=buffer)
html_buffer = buffer.getvalue()
buffer.close()
