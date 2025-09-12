
import tensorflow as tf

# Define input tensors
sparse_inputs = tf.constant([[1, 2], [3, 4], [5, 6]])
dense_inputs = tf.constant([7, 8, 9])

# Generate sparse cross from inputs
output = tf.raw_ops.SparseCross(
    indices=tf.constant([[0, 0], [1, 1]]),
    values=tf.constant([1, 2]),
    shapes=[tf.constant([3])]
)

# Print output
print(output)
