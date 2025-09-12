import tensorflow as tf

# Define your input and bias tensors
input_tensor = tf.constant([1, 2, 3, 4, 5], dtype=tf.qint8)
bias_tensor = tf.constant([6, 7, 8, 9, 10], dtype=tf.qint8)

# Use tf.math.add to add the input and the bias tensors
result_tensor = tf.math.add(input_tensor, bias_tensor)

with tf.Session() as sess:
    result = sess.run(result_tensor)
    print(result)
