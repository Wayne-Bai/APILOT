import tensorflow as tf

with tf.profiler.experimental.Trace("scope_name", epoch_tracer=True):
    # Define your TensorFlow graph and operations here
    pass
