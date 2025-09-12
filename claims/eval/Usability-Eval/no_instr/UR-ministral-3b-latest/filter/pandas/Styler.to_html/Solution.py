import pandas as pd

# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 27, 30],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)

# Convert DataFrame to HTML-CSS format
html = df.to_html(classes={'classname': 'mytable'})

# Styler example
style_dict = {
    'font-size': '25px',
    'border-collapse': 'collapse',
    'width': '100%'
}
table_style = pd.DataFrame(columns=[''])
table = table_style.style.apply(lambda x: 'width: 100%; margin: 15px 0px 15px 0px;', axis=1)

# Write to buffer
with open('output.html', 'w') as f:
    f.write("<html><head><style>" + table.get.table(label="Table", index=False, header=False, CSS=style_dict).get_html() + "</style></head><body>" + f'{html}' + "</body></html>")
    print(html)
