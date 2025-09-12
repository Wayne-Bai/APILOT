import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}
df = pd.DataFrame(data)

# Apply styling to the DataFrame
styled_df = df.style.applymap(lambda x: 'color: red' if x > 5 else 'color: black')

# Write the styled DataFrame to an HTML file
with open('styled_df.html', 'w') as f:
    f.write(styled_df.to_html())

# Write the styled DataFrame to a string
html_string = styled_df.to_html()

# Write the styled DataFrame to a buffer (BytesIO)
import io
buffer = io.StringIO()
styled_df.to_html(buffer)
html_buffer = buffer.getvalue()
buffer.close()
