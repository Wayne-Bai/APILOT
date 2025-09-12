import pandas as pd

# Load your DataFrame (replace 'your_data.csv' with your actual file)
df = pd.read_csv('your_data.csv')

# Function to convert object columns to more appropriate dtypes
def convert_object_columns(df):
    for col in df.select_dtypes(include=['object']).columns:
        # Attempt to convert to numeric if possible
        df[col] = pd.to_numeric(df[col], errors='ignore')
        # Convert to datetime if possible
        df[col] = pd.to_datetime(df[col], errors='ignore')
        # Optionally convert to category
        if df[col].dtype == 'object':
            df[col] = df[col].astype('category')
    return df

# Convert object columns in the DataFrame
df = convert_object_columns(df)

# Display the updated DataFrame dtypes
print(df.dtypes)
