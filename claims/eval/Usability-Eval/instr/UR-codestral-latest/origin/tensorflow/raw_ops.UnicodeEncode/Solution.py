import tensorflow as tf

# Create a tensor of integers
int_tensor = tf.constant([1, 2, 3, 4, 5], dtype=tf.int32)

# Encode the tensor of integers into a tensor of strings
string_tensor = tf.raw_ops.SerializeToString(input=int_tensor)

# Start a TensorFlow session
with tf.Session() as sess:
    # Run the TensorFlow operation to get the result
    result = sess.run(string_tensor)
    print(result)
