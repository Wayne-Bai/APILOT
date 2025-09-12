import pandas as pd

# Assuming you have a DataFrame like this
df = pd.DataFrame({
    'labels': ['label1', 'label2', 'label3']
})

# Add a string suffix to the labels
suffix = '_suffix'
df['labels'] = df['labels'] + suffix

print(df)
