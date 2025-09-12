import pandas as pd

# Assuming you have a DataFrame called 'df'
html_string = df.style.to_html()

# Write the HTML string to a file
with open('output.html', 'w') as f:
    f.write(html_string)
