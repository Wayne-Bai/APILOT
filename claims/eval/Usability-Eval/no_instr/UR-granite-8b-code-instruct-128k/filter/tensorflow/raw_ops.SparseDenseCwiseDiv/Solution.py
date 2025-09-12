
import tensorflow as tf

# Create SparseTensor
sparse_tensor = tf.SparseTensor(indices=[[0, 0], [1, 2]], values=[1, 2], dense_shape=[3, 4])

# Create dense tensor
dense_tensor = tf.constant([4, 5, 6, 7], dtype=tf.float32)

# Component-wise division using tf.sparse_tensor_div
result = tf.sparse_tensor_div(sparse_tensor, dense_tensor)

# Print the result
with tf.Session() as sess:
    print(sess.run(result))
