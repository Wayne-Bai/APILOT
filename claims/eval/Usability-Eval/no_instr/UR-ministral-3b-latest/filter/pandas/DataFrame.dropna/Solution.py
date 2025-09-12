import pandas as pd

# Load your dataset (replace 'your_dataset.csv' with your actual file name)
df = pd.read_csv('your_dataset.csv')

# Drop rows with any missing values
df = df.dropna()

# Save the cleaned dataset (replace 'cleaned_dataset.csv' with your desired file name)
df.to_csv('cleaned_dataset.csv', index=False)
