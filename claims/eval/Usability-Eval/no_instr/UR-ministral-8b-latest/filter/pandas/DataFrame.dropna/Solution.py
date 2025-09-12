import pandas as pd

# Load your DataFrame (replace 'your_file.csv' with your actual file name)
df = pd.read_csv('your_file.csv')

# Remove missing values
df = df.dropna()

# Save the cleaned DataFrame to a new CSV file (replace 'cleaned_file.csv' with your desired file name)
df.to_csv('cleaned_file.csv', index=False)
