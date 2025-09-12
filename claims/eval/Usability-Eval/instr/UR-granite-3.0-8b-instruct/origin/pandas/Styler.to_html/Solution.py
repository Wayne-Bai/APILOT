import pandas as pd

# Assuming df is your DataFrame
df = pd.DataFrame(...)

# Convert the DataFrame to a HTML table
html_table = df.to_html(index=False, justify='center')

# Write the HTML table to a file
with open('output.html', 'w') as f:
    f.write(html_table)
