import pandas as pd

# Load pickled pandas object
def load_pickle(filename):
    try:
        with open(filename, 'rb') as handle:
            unpickled_data = pickle.load(handle)
        return unpickled_data
    except Exception as e:
        print("Error occurred:", e)

# Test the function
filename = 'my_data.pkl'  # replace with your filename
output = load_pickle(filename)
print(output)
