import pandas as pd

# create a sample dataframe
data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)

# create a Styler object and style the dataframe
s = df.style
s.applymap(lambda x: 'color: red;' if x > 2 else '')
s.set_table_styles([{'selector': '', 'props': [('border', '1px solid black')]}])
s.set_caption("This is a caption")
s.to_html("output.html", index=False)
