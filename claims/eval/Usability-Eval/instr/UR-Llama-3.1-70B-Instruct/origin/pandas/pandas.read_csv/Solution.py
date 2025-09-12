import pandas as pd

def read_csv_file(file_path, chunk_size=None):
    try:
        if chunk_size is None:
            # Read the entire csv file into a DataFrame
            df = pd.read_csv(file_path)
            return df
        else:
            # Break the file into chunks
            chunk_list = []
            for chunk in pd.read_csv(file_path, chunksize=chunk_size):
                chunk_list.append(chunk)
            # Concatenate the chunks into a single DataFrame
            df = pd.concat(chunk_list, axis=0)
            return df
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except pd.errors.EmptyDataError:
        print(f"No data in file: {file_path}")
        return None
    except pd.errors.ParserError:
        print(f"Error parsing file: {file_path}")
        return None

# Example usage
file_path = 'data.csv'
df = read_csv_file(file_path)
print(df)

# Read the file in chunks of 1000 rows
df_chunks = read_csv_file(file_path, chunk_size=1000)
print(df_chunks)
