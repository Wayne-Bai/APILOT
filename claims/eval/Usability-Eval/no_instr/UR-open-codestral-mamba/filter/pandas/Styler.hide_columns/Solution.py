import pandas as pd

# Create data
data = {'Name': ['Tom', 'Nick', 'John'], 'Age': [20, 21, 19]}

# Create DataFrame
df = pd.DataFrame(data)

# Display DataFrame without column headers
with pd.option_context('display.show_dimensions', False):
    print(df.to_string(index=False))
