
import tensorflow as tf

# Create a tensor
tensor = tf.constant([1, 2, 3])

# Get the session handle for the current session
session = tf.get_default_session()
handle = session.run(tf.raw_ops.SessionHandle)

# Store the tensor in the state of the session
state = session.run(tf.raw_ops.Store(tensor, handle))
