import tensorflow as tf

def quantized_elementwise_multiply(x, y, min_x, max_x, min_y, max_y):
    # Define the effect quantized ranges as described
    min_output = min_x * min_y
    max_output = max_x * max_y

    # Perform the quantized multiplication
    result, output_min, output_max = tf.raw_ops.QuantizedMul(
        x=x, 
        y=y, 
        min_x=min_x, 
        max_x=max_x,
        min_y=min_y, 
        max_y=max_y, 
        Toutput=tf.quint8
    )

    return result, output_min, output_max

# Sample inputs for testing
x = tf.constant([10, 20, 30], dtype=tf.qint8)
y = tf.constant([1, 2, 3], dtype=tf.qint8)

# Define the min/max values for quantization
min_x = -128
max_x = 127
min_y = -128
max_y = 127

result, min_out, max_out = quantized_elementwise_multiply(x, y, min_x, max_x, min_y, max_y)

print("Result:", result)
print("Min Output:", min_out)
print("Max Output:", max_out)
