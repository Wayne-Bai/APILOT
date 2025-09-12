# Import necessary libraries
import tensorflow as tf
from tensorflow.python.framework import nest

print(nest.__doc__)
print(nest.__name__)

# Example usage of nest functions:
# Verify that a list of floats is a nested structure
def is_iterable(x):
  """Returns true if the structure consists entirely of anything in Python"""
  try:
    iter(x)
    return True
  except TypeError:
    return False

def is_nested(x):
  """True if x contains the empty tuple as one element."""
  return nest.is_sequence(x) and any(nest.is_sequence(x_i) for x_i in x)

print(is_nested([1.0, 2.0, 3.0])) 
print(is_nested([[1.0], [2.0], [3.0]]))

# Get the structure and items of a nested structure
nested_structure = [1, [2, 3], [4, [5, 6]]]
print(nest.map_structure(lambda x: x + 1, nested_structure))

# Flatten a nested structure
flat_structure = nest.flatten(nested_structure)
print(flat_structure)

# Get the structure of a nested structure
structure = nest.map_structure(lambda x: x.shape, [[1, 2], [3, 4]])
print(structure)

# Get the compute graph size of a nested structure
compute_graph_size = nest.map_structure(lambda x: x.size if hasattr(x,'size') else 0, tf.constant([[1, 2], [3, 4]]))
print(compute_graph_size)
