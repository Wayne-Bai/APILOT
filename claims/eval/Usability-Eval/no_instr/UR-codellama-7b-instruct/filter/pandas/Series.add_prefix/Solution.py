
import pandas as pd

# create a sample dataframe
data = {'Name': ['Alex', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'Gender': ['Male', 'Female', 'Male']}
df = pd.DataFrame(data)

# prefix the labels with the string "User_"
df.columns = df.columns.str.replace("", "User_")
print(df)
