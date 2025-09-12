import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Tom', 'Nick', 'John'],
        'Age': [20, 21, 19],
        'Country': ['USA', 'Canada', 'Mexico']}
df = pd.DataFrame(data)

# Set a caption for the table
df_styler = df.style.set_caption("Styler HTML Example")

# Use the `render` method to write to a file as an HTML string
html_string = df_styler.render()

# Save to an HTML file
with open('df_output.html', 'w') as f:
    f.write(html_string)

print("Success: DataFrame written to df_output.html file.")
