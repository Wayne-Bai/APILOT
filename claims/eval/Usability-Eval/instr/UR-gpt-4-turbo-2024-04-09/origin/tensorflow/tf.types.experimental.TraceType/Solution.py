import tensorflow as tf

@tf.function(input_signature=[tf.TensorSpec(shape=None, dtype=tf.float32)])
def function_with_tracing(x):
    return x + x

# Example usage:
tensor = tf.constant([1.0, 2.0, 3.0])
result = function_with_tracing(tensor)
print(result)
