import tensorflow as tf

def quantized_conv2d(input_tensor, filter_tensor, min_input, max_input, min_filter, max_filter, strides, padding):
    # Convert tensors to quantized tensors
    input_quantized = tf.quantization.quantize(input_tensor, min_input, max_input, tf.quint8)
    filter_quantized = tf.quantization.quantize(filter_tensor, min_filter, max_filter, tf.quint8)
    
    # Compute a 2D convolution given quantized 4D input and filter tensors.
    result = tf.raw_ops.QuantizedConv2D(
        input=input_quantized,
        filter=filter_quantized,
        min_input=min_input,
        max_input=max_input,
        min_filter=min_filter,
        max_filter=max_filter,
        strides=strides,
        padding=padding
    )
    
    return result

# Example usage:
input_tensor = tf.random.uniform(shape=(1, 10, 10, 1), minval=0, maxval=255, dtype=tf.float32)
filter_tensor = tf.random.uniform(shape=(3, 3, 1, 1), minval=0, maxval=255, dtype=tf.float32)

min_input = tf.constant(0.0)
max_input = tf.constant(255.0)
min_filter = tf.constant(0.0)
max_filter = tf.constant(255.0)
strides = [1, 1, 1, 1]
padding = 'SAME'

result = quantized_conv2d(input_tensor, filter_tensor, min_input, max_input, min_filter, max_filter, strides, padding)
print(result)
