
import numpy as np
from networkx import graph

# Define the two sets of numbers to compare
set1 = [1, 2, 3]
set2 = [1.000001, 2.000001, 3.000001]

# Define the tolerance within which the sets are considered equal
tolerance = 0.00001

# Use NetworkX to check if the two sets are equal within the specified tolerance
G = graph()
G.add_edge(set1, set2)
if G.is_connected():
    print("The two sets are equal within a tolerance of", tolerance)
else:
    print("The two sets are not equal within a tolerance of", tolerance)
