import pandas as pd

# Assuming we have a DataFrame `df`
df = pd.DataFrame({
    'A': ['foo', 'bar', 'baz'],
    'B': ['one', 'one', 'two'],
    'C': [1, 2, 3],
    'D': [10, 20, 30]
})

# Define styler object
styler = df.style

# Now we can use the Styler object's methods for formatting
styler.set_properties(**{'background-color': 'black',
                         'color': 'white'}).set_table_styles([
    dict(selector='th', props=[('background-color', 'darkred'),
                               ('color', 'white')])])

# Export to a HTML file
styler.to_excel("styled_table.xlsx")
