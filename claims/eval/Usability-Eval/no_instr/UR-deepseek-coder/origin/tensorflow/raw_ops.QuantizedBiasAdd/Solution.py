import tensorflow as tf

def quantized_add(input_tensor, bias_tensor):
    # Ensure the input and bias tensors are of the same quantized type
    input_tensor = tf.convert_to_tensor(input_tensor)
    bias_tensor = tf.convert_to_tensor(bias_tensor)
    
    # Perform the addition for quantized types
    result = tf.raw_ops.QuantizedAdd(
        x=input_tensor,
        y=bias_tensor,
        min_x=tf.reduce_min(input_tensor),
        max_x=tf.reduce_max(input_tensor),
        min_y=tf.reduce_min(bias_tensor),
        max_y=tf.reduce_max(bias_tensor)
    )
    
    return result

# Example usage:
# input_tensor = tf.constant([1, 2, 3], dtype=tf.qint8)
# bias_tensor = tf.constant([1, 1, 1], dtype=tf.qint8)
# result = quantized_add(input_tensor, bias_tensor)
# print(result)
