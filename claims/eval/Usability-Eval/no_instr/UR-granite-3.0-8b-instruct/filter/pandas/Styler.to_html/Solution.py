import pandas as pd

# Assuming df is your DataFrame
df = pd.DataFrame(...)

# Write Styler to a file
df.style.set_properties(**{'text-align': 'right'}).hide_index().set_table_attributes('class="table table-striped"').render('my_table.html')

# Write Styler to a buffer
buffer = io.StringIO()
df.style.set_properties(**{'text-align': 'right'}).hide_index().set_table_attributes('class="table table-striped"').render(buffer)

# Write Styler to a string
html_string = df.style.set_properties(**{'text-align': 'right'}).hide_index().set_table_attributes('class="table table-striped"').render()
