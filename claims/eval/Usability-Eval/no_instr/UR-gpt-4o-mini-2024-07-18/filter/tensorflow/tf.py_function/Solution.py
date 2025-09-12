import tensorflow as tf

@tf.function
def wrapped_function(x):
    return x * x + 2 * x + 1

# Example usage
x = tf.constant([1, 2, 3], dtype=tf.float32)
result = wrapped_function(x)
tf.print(result)  # Outputs: [4, 9, 16]
