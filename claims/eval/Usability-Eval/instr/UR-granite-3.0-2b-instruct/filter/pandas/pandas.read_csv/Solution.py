import pandas as pd

def read_csv_file(file_path, chunk_size=None):
    dataframes = []
    if chunk_size:
        for chunk in pd.read_csv(file_path, chunksize=chunk_size):
            dataframes.append(chunk)
    else:
        dataframes.append(pd.read_csv(file_path))
    return dataframes
