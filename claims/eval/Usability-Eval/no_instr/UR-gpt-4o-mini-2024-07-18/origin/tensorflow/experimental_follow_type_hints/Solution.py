import tensorflow as tf

def my_function(x: tf.Tensor) -> tf.Tensor:
    # Perform some operations on the tensor x
    result = tf.square(x) + 2 * x + 1
    return result

# Example usage
input_tensor = tf.constant([1.0, 2.0, 3.0])
output_tensor = my_function(input_tensor)
print(output_tensor)
