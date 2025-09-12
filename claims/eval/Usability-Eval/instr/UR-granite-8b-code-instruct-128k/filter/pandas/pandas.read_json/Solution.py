import pandas as pd

def json_to_pandas(json_string):
    return pd.read_json(json_string)
