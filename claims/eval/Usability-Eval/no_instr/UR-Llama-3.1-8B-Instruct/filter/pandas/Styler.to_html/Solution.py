import pandas as pd

# Creating a dataframe
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 24, 35, 32],
    'Country': ['USA', 'UK', 'Australia', 'Germany']
}
df = pd.DataFrame(data)

# Styling the dataframe
styled_df = df.style.applymap(lambda x: 'color: red' if x % 2 else 'color: blue')

# Writing the styled dataframe to an HTML file
styled_df.to_html('styled_df.html', render_links=True, escape=False)

# Writing the styled dataframe to a string
styled_string = styled_df.to_html()
print(styled_string)
