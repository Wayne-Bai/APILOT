
import tensorflow as tf

# Define the inputs and outputs of the operation
input_x = tf.constant([[1, 2], [3, 4]], dtype=tf.quint8)
input_y = tf.constant([[5, 6], [7, 8]], dtype=tf.quint8)
output_z = tf.quantized.mul(input_x, input_y, input_z.shape)

# Create a session and run the operation
with tf.Session() as sess:
    result = sess.run(output_z)

# Print the result
print(result)
