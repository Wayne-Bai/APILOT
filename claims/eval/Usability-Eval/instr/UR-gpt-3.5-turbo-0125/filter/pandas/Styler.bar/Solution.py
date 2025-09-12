
import pandas as pd

# Create a sample DataFrame
data = {'A': [10, 20, 30],
        'B': [15, 25, 35]}
df = pd.DataFrame(data)

# Create a function to apply background color
def color_negative_red(val):
    color = 'red' if val < 0 else 'white'
    return 'background-color: %s' % color

# Apply the function to the DataFrame
styled_df = df.style.applymap(color_negative_red)

# Display the styled DataFrame
styled_df
