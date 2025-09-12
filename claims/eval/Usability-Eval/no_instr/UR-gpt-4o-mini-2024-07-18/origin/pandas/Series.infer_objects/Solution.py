import pandas as pd

def infer_object_dtypes(df):
    for col in df.select_dtypes(include=['object']).columns:
        # Attempt to convert to category if appropriate
        if df[col].nunique() / len(df[col]) < 0.5:  # Change the threshold as needed
            df[col] = df[col].astype('category')
        # Attempt to convert to datetime
        else:
            try:
                df[col] = pd.to_datetime(df[col])
            except (ValueError, TypeError):
                pass  # If conversion fails, keep the original dtype
    return df

# Sample usage:
# df = pd.read_csv('your_file.csv')
# df = infer_object_dtypes(df)
