
import pandas as pd

# create a styler object
styler = df.style

# define the file path where you want to save the styled data
file_path = 'my_data.html'

# write the styled data to a file in HTML-CSS format
with open(file_path, 'w') as f:
    f.write(styler.render())
