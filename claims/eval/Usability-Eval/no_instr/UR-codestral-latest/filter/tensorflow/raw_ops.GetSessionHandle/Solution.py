import tensorflow as tf

with tf.Session() as sess:
    input_tensor = tf.constant([1, 2, 3, 4, 5])  # Your input tensor
    tensor_handle = sess.run(tf.raw_ops.HandleFromTensor(tensor=input_tensor).handle)

# Now, tensor_handle can be used to access the value of the input_tensor in the current session
