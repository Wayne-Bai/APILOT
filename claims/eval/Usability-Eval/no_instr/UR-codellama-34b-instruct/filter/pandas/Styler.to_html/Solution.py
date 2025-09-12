
import pandas as pd

# create a sample DataFrame
df = pd.DataFrame({'Name': ['John', 'Amy', 'Bob'],
                   'Age': [25, 30, 28],
                   'Gender': ['Male', 'Female', 'Male']})

# define the HTML-CSS style for the DataFrame
style = '''
<style>
table {
    border: 1px solid black;
    border-collapse: collapse;
}
th, td {
    padding: 8px;
    text-align: left;
    border-bottom: 1px solid #ddd;
}
tr:nth-child(even) {background-color: #f2f2f2;}
</style>
'''

# create a HTML-CSS string from the DataFrame using the style
html = df.to_html(table_id='my_table', classes=['table', 'table-striped'], index=False, escape=False)

# write the HTML-CSS string to a file or buffer
with open('df.html', 'w') as f:
    f.write(style + html)
