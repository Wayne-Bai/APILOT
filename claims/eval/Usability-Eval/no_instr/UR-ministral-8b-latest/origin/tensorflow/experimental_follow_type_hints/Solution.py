import tensorflow as tf

def custom_function(input_tensor: tf.Tensor, type_annotation: bool = False) -> tf.Tensor:
    if type_annotation:
        # Placeholder for potential optimization based on type annotations
        pass
    else:
        # Implement your computational graph using TensorFlow operations
        result = input_tensor * 2  # Example operation
        return result

# Example usage:
input_data = tf.constant([1.0, 2.0, 3.0], dtype=tf.float32)
output_data = custom_function(input_data, type_annotation=True)
print(output_data)
