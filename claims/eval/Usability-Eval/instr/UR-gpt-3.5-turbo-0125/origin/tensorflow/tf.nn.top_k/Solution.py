
import tensorflow as tf

# Define the input tensor
input_tensor = tf.constant([[1, 3, 2],
                            [4, 6, 5],
                            [7, 9, 8]])

# Find the values and indices of the k largest entries along the last dimension
k = 2
values, indices = tf.math.top_k(input_tensor, k=k)

# Start a TensorFlow session
with tf.Session() as sess:
    values_result, indices_result = sess.run([values, indices])

print("Top {} values:".format(k), values_result)
print("Top {} indices:".format(k), indices_result)
