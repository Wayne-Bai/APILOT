# Import pandas library
import pandas as pd

# Create a sample DataFrame
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 24, 35, 32],
    'Country': ['USA', 'UK', 'Australia', 'Germany']
}
df = pd.DataFrame(data)

# Create a styler object
styler = df.style.set_table_attributes(['border="1" cellpadding="10"']) \
               .set_caption('Sample DataFrame') \
               .set_html_attributes('.container {max-width: 800px;}')

# Write styler to a file
with open('sample_table.tex', 'w') as file:
    styler.dump(file, flavor='latex')

# Write styler to a buffer (stdout)
print(styler.to_latex(writing_options={'longtable': True, 'table_attributes': 'border="1" cellpadding="10"'}))

# Write styler to a string
latex_string = styler.to_latex(writing_options={'longtable': True, 'table_attributes': 'border="1" cellpadding="10"'})
print(latex_string)
