import tensorflow as tf

# Create a TensorFlow session
with tf.Session() as sess:
    # Create a variable to store the input data
    x = tf.Variable(tf.zeros([10, 5]))
    
    # Create an indices tensor
    i = tf.constant([[2], [4], [7]])
    
    # Use the Gather operation to select slices from x according to the indices in i
    y = tf.raw_ops.Gather(params=x, indices=i)
    
    # Print the resulting tensor
    print(sess.run(y))
