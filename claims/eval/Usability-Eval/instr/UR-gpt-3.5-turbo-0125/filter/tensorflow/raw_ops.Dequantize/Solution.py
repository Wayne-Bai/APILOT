
import tensorflow as tf

def dequantize_input(input_tensor):
    # Dequantize the input tensor into a float or bfloat16 tensor
    # Use the tf.cast function to cast the input tensor to float
    float_tensor = tf.cast(input_tensor, tf.float32)  # Change tf.float32 to tf.bfloat16 if bfloat16 is needed
    return float_tensor

# Example usage
input_tensor = tf.constant([1, 2, 3], dtype=tf.int8)
dequantized_tensor = dequantize_input(input_tensor)
print(dequantized_tensor)
