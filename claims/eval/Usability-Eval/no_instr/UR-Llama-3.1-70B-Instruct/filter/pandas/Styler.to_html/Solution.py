# Importing necessary library
import pandas as pd

# Creating a DataFrame
df = pd.DataFrame({
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 24, 35, 32],
    'Country': ['USA', 'UK', 'Australia', 'Germany']
})

# Creating a Styler object
styler = df.style

# Writing the Styler to an HTML file
styler.to_html('styled_table.html')

# Writing the Styler to a buffer (in this case, a StringIO object)
from io import StringIO
buffer = StringIO()
styler.to_html(buffer)
print(buffer.getvalue())

# Writing the Styler to a string
html_string = styler.to_html()
print(html_string)
