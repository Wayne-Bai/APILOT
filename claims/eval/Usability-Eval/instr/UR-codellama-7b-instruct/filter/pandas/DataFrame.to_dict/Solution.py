import pandas as pd

# create a sample DataFrame
data = {'Name': ['John', 'Doe'], 'Age': [25, 30], 'Gender': ['Male', 'Female']}
df = pd.DataFrame(data)

# convert the DataFrame to a dictionary
dictionary = df.to_dict()

print(dictionary)
