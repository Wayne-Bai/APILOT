import pandas as pd

# create a sample dataframe
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['NYC', 'LA', 'Chicago']}
df = pd.DataFrame(data)

# create a styler object
styler = df.style

# add some styles to the dataframe
styler.set_properties(**{'background-color': '#f5f5f5'})
styler.set_table_styles([('border', '1px solid #ccc')])
styler.set_caption("My Styled Dataframe")

# write the styled dataframe to an HTML file
with open('styled_df.html', 'w') as f:
    styler.to_html(f)
