import numpy as np

def load_data(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            values = [float(val.strip()) for val in line.split() if val.strip()]
            data.append(values)
    data_array = np.array(data)
    return data_array

file_path = 'data.txt'
data = load_data(file_path)
print(data)
