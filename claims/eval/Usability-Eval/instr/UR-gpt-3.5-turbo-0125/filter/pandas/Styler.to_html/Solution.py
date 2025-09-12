
import pandas as pd

# Create a DataFrame for example
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)

# Styling the DataFrame
styles = df.style.set_table_styles([{'selector': 'th', 'props': [('border', '1px solid black')]}])

# Write Styler to a file
with open('styled_table.html', 'w') as f:
    f.write(styles.render())

# This will generate an HTML file with the styled table
