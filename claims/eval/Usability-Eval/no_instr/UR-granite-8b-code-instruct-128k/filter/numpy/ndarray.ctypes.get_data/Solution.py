import numpy as np

def get_array_memory(array):
    return array.__array_interface__['data'][0]
