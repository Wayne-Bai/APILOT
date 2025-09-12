# Import necessary libraries
import pandas as pd

# Function to infer better dtypes for object columns
def infer_object_dtypes(df):
    # Iterate over object columns
    for col in df.select_dtypes(include=['object']).columns:
        # Try to infer better dtype
        try:
            df[col] = pd.to_numeric(df[col], errors='coerce')
            if pd.api.types.is_numeric_dtype(df[col]):
                continue
        except ValueError:
            pass
        
        # Try to obtain better dtype by using more specific converters
        converters = {
            'category': lambda x: pd.Categorical(x).codes,
            'datetime64[ns]': pd.to_datetime,
            'timedelta64[ns]': lambda x: pd.to_timedelta(x, box=False)
        }
        
        # Get dtype of each object column
        dtype = df[col].dtype
        
        # Use more specific converters if possible
        converter = converters.get(dtype.name, None)
        if converter:
            try:
                df[col] = df[col].apply(converter)
            except Exception as e:
                print(f"Failed to convert {col} to {dtype.name}: {str(e)}")
        
        # If previous attempts failed, use categorical dtype for better performance
        else:
            try:
                df[col] = pd.Categorical(df[col]).codes
            except Exception as e:
                print(f"Failed to convert {col} to categorical: {str(e)}")
    
    return df

# Usage
if __name__ == "__main__":
    # Create a sample DataFrame
    data = {
        'A': [1, 2, 3],
        'B': ['a', 'b', 'c'],
        'C': ['2022-01-01', '2022-01-02', '2022-01-03'],
        'D': ['10:00:00', '11:00:00', '12:00:00']
    }
    df = pd.DataFrame(data)
    
    # Infer better dtypes for object columns
    inferred_df = infer_object_dtypes(df)
    
    print(inferred_df)
