import scipy.ndimage

def multidimensional_minimum_filter(data, size=3):
    return scipy.ndimage.minimum_filter(data, size=size)

# Example usage:
# data = np.random.rand(5,5)
# filtered_data = multidimensional_minimum_filter(data, size=2)
# print(filtered_data)
