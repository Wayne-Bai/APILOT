# Importing required libraries
import networkx as nx
import numpy as np
import collections

# Create a sample dictionary of numbers
numbers = {
    'apple': 3,
    'banana': 4,
    'cherry': 5,
    'date': 2
}

# Define a mapping if needed
# For simplicity, assuming a one-to-one mapping with no need for different keys
# If a specific mapping is needed, define it here
mapping = None  # Set this as per your requirement

if mapping:
    mapped_numbers = {k: v for k, v in mapping.items()}
else:
    mapped_numbers = numbers

# Convert the dictionary to a 1D numpy array
numbers_array = np.array(list(mapped_numbers.values()))

print(numbers_array)
