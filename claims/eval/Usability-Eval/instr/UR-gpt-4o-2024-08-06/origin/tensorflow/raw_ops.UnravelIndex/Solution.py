import tensorflow as tf

# Create a TensorFlow function to convert flat indices into tuples of coordinates
def unravel_indices(flat_indices, dims):
    # Calculate the cumulative product of dims, which represents the strides in the flattened array
    strides = tf.math.cumprod(dims, exclusive=True, reverse=True)
    
    # Create an array to hold the coordinates
    coordinates = []
    
    # Iterate over the dimensions
    for stride in strides:
        # Find the coordinate for the current dimension and update the flat indices
        coordinate = flat_indices // stride
        flat_indices = flat_indices % stride
        coordinates.append(coordinate)
    
    # Return the stack of coordinates
    return tf.stack(coordinates, axis=-1)

# Example usage
flat_indices = tf.constant([22, 41])
dims = tf.constant([4, 5, 6])
coord_arrays = unravel_indices(flat_indices, dims)

print(coord_arrays.numpy())  # Output the coordinates in NumPy format
