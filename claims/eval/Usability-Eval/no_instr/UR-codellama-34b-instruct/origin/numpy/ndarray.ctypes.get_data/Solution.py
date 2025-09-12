import numpy as np

def get_array_memory_area(arr):
    return arr.__array_interface__['data'][0]
