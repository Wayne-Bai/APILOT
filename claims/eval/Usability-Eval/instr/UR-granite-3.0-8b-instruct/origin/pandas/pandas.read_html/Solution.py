import pandas as pd

# List of file paths
file_paths = ['file1.html', 'file2.html', 'file3.html']

# List to store DataFrame objects
dfs = []

# Loop through each file path
for path in file_paths:
    # Read HTML table into a DataFrame
    df = pd.read_html(path, flavor='lxml')[0]  # Adjust the index as needed
    # Append DataFrame to the list
    dfs.append(df)

# Print the list of DataFrame objects
for df in dfs:
    print(df)
