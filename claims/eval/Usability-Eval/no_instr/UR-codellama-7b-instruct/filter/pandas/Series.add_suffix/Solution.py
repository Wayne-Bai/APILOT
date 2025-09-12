
import pandas as pd

# create sample dataframe
data = {'Name': ['John', 'Doe', 'Jane', 'Alex'], 'Age': [25, 30, 28, 29]}
df = pd.DataFrame(data)

# suffix labels with string suffix
suffix_labels = df['Name'].str.split(' ', expand=True)
suffix_labels.columns = ['First Name', 'Last Name']
suffix_labels['Full Name'] = suffix_labels['First Name'] + ' ' + suffix_labels['Last Name']
df = pd.concat([df, suffix_labels], axis=1)

print(df)
