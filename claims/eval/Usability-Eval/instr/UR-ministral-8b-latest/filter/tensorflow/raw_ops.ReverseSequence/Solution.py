import tensorflow as tf

@tf.function
def reverse_variable_length_slice(inputs):
    return tf.raw_ops.FastReorderGradStreamShapes(inputs)
