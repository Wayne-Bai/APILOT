import tensorflow as tf

@tf.function(input_signature=[tf.TensorSpec(shape=[None], dtype=tf.float32)])
def optimized_function(x):
    # Function that uses TensorFlow's graph execution
    return tf.square(x)

# Example usage
# Prepare a tensor of float32 type
tensor_input = tf.constant([1.0, 2.0, 3.0], dtype=tf.float32)

# Execute the optimized function
result = optimized_function(tensor_input)

# Print the result
print(result)
