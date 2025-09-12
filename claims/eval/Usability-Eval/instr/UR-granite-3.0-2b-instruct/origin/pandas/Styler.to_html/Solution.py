import pandas as pd
from pandas.io.html import to_html

# Assuming df is your DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})

# Write Styler to a file
df.style.to_html("styles.html", escape=False)

# Write Styler to a buffer
buffer = io.StringIO()
df.style.to_html(buffer, escape=False)
html_buffer = buffer.getvalue()

# Write Styler to a string
html_string = df.style.to_html(escape=False)

# Convert HTML to HTML-CSS format
html_css = to_html(df.styles, full_width=False)

# Print the HTML-CSS format
print(html_css)
