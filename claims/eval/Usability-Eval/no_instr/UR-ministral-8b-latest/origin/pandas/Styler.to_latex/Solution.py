import pandas as pd
import io

# Sample data to demonstrate the functionality
data = {
    'Column_1': [1, 2, 3],
    'Column_2': ['A', 'B', 'C']
}

df = pd.DataFrame(data)

# Create a Styler object
styler = df.style

# Write Styler to a file
with open('table.tex', 'w') as f:
    f.write(styler.render().lavendermode('lavendermode_name'))

# Alternatively, write to a buffer
buffer = io.StringIO()
buffer.write(styler.render().lavendermode('lavendermode_name'))
buffer.seek(0)
print(buffer.getvalue())

# Finally, write to a string
rendered_string = styler.render().lavendermode('lavendermode_name')
print(rendered_string)
