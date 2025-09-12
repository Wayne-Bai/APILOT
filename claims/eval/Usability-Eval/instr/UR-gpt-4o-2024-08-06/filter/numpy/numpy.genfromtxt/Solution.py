import numpy as np

# Define a helper function to convert missing values to NaN
def _missing_to_nan(val, missing_char="?"):
    try:
        return float(val)
    except ValueError:
        return np.nan if val == missing_char else float(val)

# Load data from the text file with missing values specified by '?'
filename = 'data.txt'  # Path to your text file
data = np.loadtxt(filename, delimiter=',', converters={i: _missing_to_nan for i in range(0, 10)})

print(data)
