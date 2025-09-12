import pandas as pd
import json

def json_to_pandas(json_string):
    """
    Convert a JSON string to a pandas DataFrame.

    Args:
    json_string (str): A string representing the JSON data.

    Returns:
    pandas.DataFrame: A pandas DataFrame representation of the JSON data.
    """
    try:
        # Load the JSON string
        json_data = json.loads(json_string)
        
        # Convert the JSON data to a pandas DataFrame
        df = pd.json_normalize(json_data)
        
        return df
    
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        return None

# Example usage
json_string = '[{"name": "John", "age": 30, "city": "New York"}, {"name": "Alice", "age": 25, "city": "Los Angeles"}]'
df = json_to_pandas(json_string)

if df is not None:
    print(df)
