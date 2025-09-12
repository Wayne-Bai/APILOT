from scipy.spatial import distance

# Define two boolean 1-D arrays
arr1 = [True, False, True, False, False]
arr2 = [False, False, True, True, False]

# Compute Kulsinski dissimilarity
dissimilarity = distance.kulsinski(arr1, arr2)

print("Kulsinski dissimilarity:", dissimilarity)
