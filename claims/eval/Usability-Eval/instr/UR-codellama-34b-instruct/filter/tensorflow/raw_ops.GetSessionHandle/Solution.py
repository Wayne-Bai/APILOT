
import tensorflow as tf

# Create a session object
session = tf.Session()

# Create a placeholder for the input tensor
input_tensor = tf.placeholder(dtype=tf.float32, shape=[None])

# Store the input tensor in the session state
session.run(tf.raw_ops.StoreSessionTensor(
    input_tensor=input_tensor,
    key="my_tensor",
    session=session))
