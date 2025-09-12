import pandas as pd
from io import StringIO

# Create an example DataFrame
df = pd.DataFrame({
    'Column1': [1, 2, 3],
    'Column2': ['A', 'B', 'C']
})

# Create a Styler instance
styler = df.style

# Apply styling using HTML and CSS
styled_html = styler.set_properties(subset=pd.IndexSlice[:, 'Column1'], fontweight='bold').set_properties(background='yellow')

# Raise the HTML-SCSS string as Variable into buffer
html_buffer = styled_html.to_html()

# Write Styler to a .html file
with open('styled_table.html', 'w') as f:
    f.write(html_buffer)
