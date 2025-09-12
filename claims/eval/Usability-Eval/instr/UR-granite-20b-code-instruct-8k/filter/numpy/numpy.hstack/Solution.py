import numpy as np

# Assuming you have two arrays, a and b, you can stack them horizontally using the following code:

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

c = np.hstack((a, b))

# The output will be a new array, c, which contains the elements of a and b stacked horizontally:

print(c)
