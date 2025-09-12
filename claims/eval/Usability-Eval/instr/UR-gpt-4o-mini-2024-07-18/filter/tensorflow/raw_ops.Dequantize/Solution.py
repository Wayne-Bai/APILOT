import tensorflow as tf

def dequantize_tensor(input_tensor, scale, zero_point):
    # Convert the input tensor using scale and zero_point
    # The input tensor is assumed to be of integer type
    float_tensor = tf.cast(input_tensor, tf.float32) * scale + zero_point
    return float_tensor

# Example usage
# input_tensor: a quantized integer tensor
# scale: the scale factor used for quantization
# zero_point: the zero point used for quantization
input_tensor = tf.constant([0, 128, 255], dtype=tf.int32)
scale = 0.01
zero_point = -1.0

result = dequantize_tensor(input_tensor, scale, zero_point)
print(result)
