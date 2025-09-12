
import tensorflow as tf

resource = ... # create a TensorFlow Resource object
indices = ... # create a TensorFlow tensor of int32 indices

gather_output = tf.raw_ops.Gather(params=resource, indices=indices)

# Alternatively, you can use the `tf.gather` function which is a high-level wrapper for the Gather op
gather_output = tf.gather(params=resource, indices=indices)
