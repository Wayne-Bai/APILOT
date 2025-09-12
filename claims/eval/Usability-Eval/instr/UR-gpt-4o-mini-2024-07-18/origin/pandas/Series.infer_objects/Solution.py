import pandas as pd

def infer_dtypes(df):
    for col in df.select_dtypes(include=['object']).columns:
        # Attempt to infer better dtypes
        if df[col].str.isnumeric().all():
            df[col] = pd.to_numeric(df[col])
        elif df[col].str.isdate().all():
            df[col] = pd.to_datetime(df[col])
        # Add more type inference logic if needed
    return df

# Example usage:
# df = pd.read_csv('your_file.csv')  # Replace with your actual data loading method
# df = infer_dtypes(df)
