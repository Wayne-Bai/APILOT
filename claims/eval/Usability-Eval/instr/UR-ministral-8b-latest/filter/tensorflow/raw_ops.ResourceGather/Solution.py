import tensorflow as tf

def gather_from_tensor(tensor, indices):
    return tf.raw_ops.GatherV2(indices=indices, params=tensor)

# Example usage
tensor = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
indices = tf.constant([[0, 1], [1, 2]])

result = gather_from_tensor(tensor, indices)
print(result)
