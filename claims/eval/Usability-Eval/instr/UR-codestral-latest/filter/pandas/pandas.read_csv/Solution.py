import pandas as pd

def read_csv_chunked(file_path, chunk_size=None):
    # If chunk_size is not specified, read the entire file at once
    if chunk_size is None:
        df = pd.read_csv(file_path)
        return [df]
    else:
        # If chunk_size is specified, read the file in chunks
        chunks = []
        for chunk in pd.read_csv(file_path, chunksize=chunk_size):
            chunks.append(chunk)
        return chunks
