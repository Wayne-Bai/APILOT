import pandas as pd

# Let's assume we have a dataframe df
data = {'Name': ['John', 'Anna', 'Peter'],
        'Age': [28, 23, 29]}
df = pd.DataFrame(data)

# Add CSS Styles
styles = [{'selector': 'th', 'props': [('background-color', 'blue'), ('color', 'white')]},
          {'selector': 'td', 'props': [('background-color', 'green')]}]

# To HTML with CSS
html = df.to_html(classes="styled", index=False)
html = html.replace('dataframe styled', 'styled-table')
html = html.replace('<table ', '<table style="border-collapse: collapse;" ')
df.to_html(open('styled.html', 'a'), classes="styled", index=False) # writing it to file
