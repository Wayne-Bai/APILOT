import scipy.ndimage

def multidimensional_rank_filter(input_array, rank):
    """
    This function applies a multidimensional rank filter on an input array.
    """
    # Define the rank filter structure with the given rank
    rank_filter_structure = scipy.ndimage.generate_binary_structure(rank, 1)

    # Apply the rank filter on the input array
    filtered_array = scipy.ndimage.maximum_filter(input_array, footprint=rank_filter_structure)

    return filtered_array

# Test the function
input_array = [[[3, 1, 4], [2, 5, 2]],
               [[1, 2, 6], [3, 1, 1]],
               [[2, 1, 3], [5, 2, 2]]]

filtered_array = multidimensional_rank_filter(input_array, rank=2)
print(filtered_array)
