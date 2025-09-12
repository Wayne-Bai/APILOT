from scipy.spatial.distance import kulsinski

# Assuming x and y are two boolean 1-D arrays
x = [True, False, True, True, False]
y = [True, True, False, True, False]

print(kulsinski(x, y))
