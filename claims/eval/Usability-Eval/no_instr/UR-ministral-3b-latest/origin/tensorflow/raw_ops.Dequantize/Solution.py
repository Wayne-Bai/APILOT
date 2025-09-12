import tensorflow as tf

def dequantize(input_tensor):
    # Define the dequantize operation using tf.raw_ops
    dequantized_tensor = tf.raw_ops.DEQUANTIZE(
        input=input_tensor,
        scale=tf.constant([128.0 / 255.0]),  # Example scale, adjust as needed
        zero_point=tf.constant([0], dtype=tf.int32))  # Example zero_point, adjust as needed
    return dequantized_tensor

# Example usage
input_data = tf.constant([100, 255, 150])
dequantized_data = dequantize(input_data)
print(dequantized_data)
