
import tensorflow as tf

# Define input tensors
tensor_a = tf.constant([1, 2, 3, 4])
tensor_b = tf.constant([10, 20, 30, 40])

# Element-wise multiplication operation
result = tf.multiply(tensor_a, tensor_b)

# Run the operation in a TensorFlow session
with tf.Session() as sess:
    output = sess.run(result)
    print(output)
