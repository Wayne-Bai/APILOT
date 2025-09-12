import pandas as pd

# Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Gender': ['F', 'M', 'M']
}

df = pd.DataFrame(data)

# Create a Styler object
styler = df.style

# Apply some styling (optional)
styler = styler.highlight_max(subset=['Age'], color='yellow')

# Write the Styler to an HTML string
html_str = styler.render()

# Alternatively, write the Styler to an HTML file
with open('output.html', 'w') as file:
    file.write(html_str)
