import tensorflow as tf

def optimized_function(x: tf.Tensor) -> tf.Tensor:
    # Example operation: multiply the input tensor by 2
    return x * 2

# Example usage
input_tensor = tf.constant([1, 2, 3])
output_tensor = optimized_function(input_tensor)

print(output_tensor)
