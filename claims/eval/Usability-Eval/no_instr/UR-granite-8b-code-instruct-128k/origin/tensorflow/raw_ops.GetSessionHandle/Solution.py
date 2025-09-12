import tensorflow as tf

# Create a tensor
tensor = tf.constant([1, 2, 3])

# Create a Save operation
save_op = tf.raw_ops.Save(
    filename="/tmp/my_tensor.txt",
    tensor_names=["my_tensor"],
    data=[tensor]
)

# Add the operation to the default graph
tf.add_to_collection(tf.GraphKeys.Saver_ops, save_op)

# Create a session and run the operation
with tf.Session() as sess:
    sess.run(save_op)
