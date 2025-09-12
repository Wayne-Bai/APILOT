import pandas as pd
from io import StringIO

# Assume df is your DataFrame
df = pd.DataFrame({
    'A': ['winter', 'spring', 'summer', 'autumn'],
    'B': ['cold', 'warm', 'hot', 'mild'],
    'C': [1, 2, 3, 4],
    'D': [5, 6, 7, 8]
})

# Apply pandas style
styled = df.style.set_properties(**{'background-color': 'white',
                                     'color': 'black',
                                     'border-color': 'black'})

# Write Styler to a file in HTML-CSS format
styled.to_html("styled.html")

# Write Styler to a string in HTML-CSS format
string = StringIO()
styled.to_html(string)
string.getvalue()

# Alert: Using the to_html() function without arguments will return a string
html = df.style.to_html()  # Set this value to a variable or use it directly as needed.
