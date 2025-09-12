import tensorflow as tf

# Create two tensors
tensor1 = tf.constant([1, 2, 3, 4])
tensor2 = tf.constant([5, 6, 7, 8])

# Perform element-wise multiplication
product = tf.multiply(tensor1, tensor2)

# Print the result
with tf.Session() as sess:
    result = sess.run(product)
    print(result)
