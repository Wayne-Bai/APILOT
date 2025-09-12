import pandas as pd

def infer_dtypes(df):
    for column in df.select_dtypes(include=['object']).columns:
        # Use the pandas function to check the unique values and their counts
        num_unique_values = df[column].nunique()
        num_total_values = df[column].size

        # If there are many unique values, retain as object type
        if num_unique_values / num_total_values < 0.5:
            df[column] = df[column].astype('category')
    
    return df

# Example usage:
# df = pd.read_csv('your_file.csv')  # Make sure to use a proper way to read your DataFrame
# df = infer_dtypes(df)
