
import tensorflow as tf

# Define the input tensor shape and dtype
input_shape = (32, 10)
input_dtype = tf.int32

# Create the flattened index tensor
flattened_indices = tf.random.uniform(input_shape, minval=0, maxval=100, dtype=input_dtype)

# Define the mapping function to convert flat indices to coordinates
def coordinate_map_fn(flat_index):
  x, y = tf.math.divmod(flat_index, input_shape[1])
  return (x, y)

# Apply the mapping function to the flattened indices tensor using `map_fn`
coordinates = tf.map_fn(coordinate_map_fn, flattened_indices, dtype=tf.int32)

print("Flattened indices:", flattened_indices)
print("Coordinates:", coordinates)
