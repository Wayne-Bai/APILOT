
import pandas as pd

# Create a sample dataframe
data = {'Name': ['John', 'Jane', 'Bob'],
        'Age': [25, 34, 47],
        'Gender': ['Male', 'Female', 'Male']}
df = pd.DataFrame(data)

# Hide entire index
df = df.style.hide_index()

# Hide specific rows and columns
df = df.style.hide(['Name', 'Age'])
