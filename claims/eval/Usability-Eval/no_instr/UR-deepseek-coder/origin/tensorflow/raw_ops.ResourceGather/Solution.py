import tensorflow as tf

def gather_slices(resource, indices):
    # Gather slices from the variable pointed to by resource according to indices
    gathered_slices = tf.gather(resource, indices)
    return gathered_slices

# Example usage:
# Assuming 'resource' is a TensorFlow variable and 'indices' is a list of indices
# resource = tf.Variable([[1, 2], [3, 4], [5, 6]])
# indices = [0, 2]
# gathered = gather_slices(resource, indices)
# print(gathered.numpy())  # Output: [[1, 2], [5, 6]]
