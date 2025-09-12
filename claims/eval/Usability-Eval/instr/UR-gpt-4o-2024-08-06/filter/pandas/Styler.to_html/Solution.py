import pandas as pd

# Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 25, 23],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

# Create a Styler object with some simple styling
styled_df = df.style.set_table_styles(
    [{'selector': 'tr:hover',
      'props': [('background-color', '#f0f0f0')]},
     {'selector': 'th',
      'props': [('font-size', '110%'), ('text-align', 'center')]}]
).highlight_max(axis=0)

# Render the styled DataFrame to an HTML string
html_string = styled_df.render()

# Write the HTML string to a file
with open('styled_table.html', 'w') as f:
    f.write(html_string)

# Optionally, you can print the HTML string to verify
# print(html_string)
