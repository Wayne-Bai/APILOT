import numpy as np

def load_data(file_path):
    data = np.genfromtxt(file_path, delimiter=',', skip_header=1, filling_values=0, invalid_index=-1)
    return data
