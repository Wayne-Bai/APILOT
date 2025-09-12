import tensorflow as tf

def add_bias_to_quantized_input(input_tensor, bias_tensor, input_dtype=tf.float32, bias_dtype=tf.float32):
    # Ensure the input and bias tensors are appropriately quantized
    input_tensor = tf.cast(input_tensor, input_dtype)
    bias_tensor = tf.cast(bias_tensor, bias_dtype)

    # Add bias to input tensor
    output_tensor = tf.add(input_tensor, bias_tensor)
    
    return output_tensor
