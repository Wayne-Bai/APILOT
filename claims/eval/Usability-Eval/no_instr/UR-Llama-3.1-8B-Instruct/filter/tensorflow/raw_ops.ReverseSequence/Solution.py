import tensorflow as tf

# Creates a tensor with variable length slices
volumes = tf.constant([
    [[1, 2, 3, 4], [5, 6, 7, 8]],
    [[9, 10, 11, 12], [13, 14, 15, 16], [17, 18, 19, 20]],
])

# Reverses variable length slices using tf.raw_ops
result = tf.raw_ops.SliceInputReverse(input=volumes, begin=[
                                    0], size=[4])

# Printing the result
print(result.numpy())
