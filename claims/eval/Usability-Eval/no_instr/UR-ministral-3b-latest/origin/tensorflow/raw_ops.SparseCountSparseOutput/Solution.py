import tensorflow as tf

# Example usage of method in tf.raw_ops for sparse bin counting
input_data = [[10], [3, 5, 9], [1, 4, 8, 12]]
input_data = tf.ragged.constant(input_data)

output = tf.raw_ops.SparseReduceMean(input_data, axes=0, keepdim=True)

print(output.numpy())
