
import pandas as pd

# Create a dataframe
data = {'A': [1, 2, 3, 4],
        'B': [5, 6, 7, 8],
        'C': [9, 10, 11, 12]}
df = pd.DataFrame(data)

html = df.style.render()

# Writing the html to a file
with open('styled_table.html', 'w') as f:
    f.write(html)

# Alternatively, you can save the styled html to a string
html_string = df.style.render()

# Printing the styled html as a string
print(html_string)
