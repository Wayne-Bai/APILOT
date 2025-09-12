import scipy as sp

def kulsinski_dissimilarity(array1, array2):
    # Ensure both arrays are the same length
    assert len(array1) == len(array2)

    # Calculate the number of positions at which the arrays differ
    num_diff = sp.count_nonzero(array1 != array2)

    # Calculate the total number of positions in the arrays
    num_pos = len(array1)

    # Compute the Kulsinski dissimilarity
    kulsinski_diss = num_diff / (num_pos * (num_pos - 1) / 2)

    return kulsinski_diss

# Test the function
array1 = sp.array([True, False, True, True, False])
array2 = sp.array([False, True, True, True, True])
print(kulsinski_dissimilarity(array1, array2))
