import tensorflow as tf

def dequantize_tensor(input_tensor):
    shape = input_tensor.shape
    dtype = tf.float32 if 'float' in input_tensor.dtype else tf.bfloat16
    raw_input_tensor = tf.raw_ops.Dequantize(input_=input_tensor, scale_=tf.constant(1.0, dtype=tf.float32), zero_point_=tf.constant(0, dtype=tf.int32))
    return tf.reshape(raw_input_tensor, shape.as_list(), dtype)

# Usage
input_tensor = tf.constant([0.1, 0.2, 0.3], tf.uint8)
output_tensor = dequantize_tensor(input_tensor)
print(output_tensor)
