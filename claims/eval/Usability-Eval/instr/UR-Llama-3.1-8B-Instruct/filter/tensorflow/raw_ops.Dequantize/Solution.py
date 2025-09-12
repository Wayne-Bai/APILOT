import tensorflow as tf

def dequantize_tensor(input_tensor, input_type):
    """
    Dequantize the 'input' tensor into a float or bfloat16 Tensor.

    Args:
    input_tensor: The tensor to be dequantized.
    input_type: The type of the input tensor. Can be either float32 or bfloat16.

    Returns:
    A float or bfloat16 tensor after dequantization.
    """
    
    # Check if the input type is supported
    if input_type not in [tf.float32, tf.bfloat16]:
        raise ValueError("Input type must be either float32 or bfloat16.")
    
    # Use tf.cast to dequantize the input tensor to float32
    # If the input type is bfloat16, this will automatically convert it to float32
    dequantized_tensor = tf.cast(input_tensor, dtype=tf.float32)
    
    return dequantized_tensor

# Create a sample tensor
input_tensor = tf.constant([1.0, 2.0, 3.0, 4.0], dtype=tf.bfloat16)

print("Input Tensor:")
print(input_tensor)

# Dequantize the input tensor
dequantized_tensor = dequantize_tensor(input_tensor, tf.bfloat16)

print("\nDequantized Tensor:")
print(dequantized_tensor)
