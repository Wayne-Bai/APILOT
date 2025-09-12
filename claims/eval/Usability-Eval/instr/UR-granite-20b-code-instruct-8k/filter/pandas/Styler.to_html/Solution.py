import pandas as pd

# Assuming you have a DataFrame called 'df'

# Create a Styler object
styler = df.style

# Write the Styler to a file in HTML-CSS format
with open('output.html', 'w') as f:
    f.write(styler.to_html(justify='center'))
