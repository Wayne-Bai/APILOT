import networkx as nx
from numpy import allclose

# Define two sets of numbers that we want to compare
num1 = [1.0, 2.0, 3.0, 4.0]
num2 = [1.0001, 1.9999, 3.0, 4.0]

# Use allclose function from numpy module to assert if the two lists are equal within a tolerance
tolerance = 0.001  # You can adjust this value based on your requirements

result = allclose(num1, num2, atol=tolerance)

if result:
    print("The two lists are equal within the given tolerance.")
else:
    print("The two lists are not equal within the given tolerance.")
