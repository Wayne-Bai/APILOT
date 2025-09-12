import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Function to apply transformer to columns of a DataFrame
def apply_transformers_to_df(df, transformers):
    transformed_df = df.copy()
    for col, transformer in transformers.items():
        if col in df.columns:
            transformed_df[col] = transformer.transform(df[[col]])
        else:
            print(f"Column {col} not found in DataFrame. Skipping...")
    return transformed_df

# Example usage
if __name__ == "__main__":
    # Sample DataFrame
    data = {
        'column1': np.array([1, 2, 3, 4]),
        'column2': np.array([2, 4, 6, 8]),
        'column3': np.array([0.5, 1.5, 2.5, 3.5])
    }
    df = pd.DataFrame(data)

    # Define transformers
    transformers = {
        'column1': StandardScaler(),
        'column2': StandardScaler()
    }

    # Apply transformers
    transformed_df = apply_transformers_to_df(df, transformers)

    print(transformed_df)
