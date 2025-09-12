import tensorflow as tf

quantize_input = tf(input_tensor)   # You would need to replace input_tensor with your actual tensor
dequantize_input = tf.dequantize(quantize_input)
image_original_shape = tf.raw_ops.QuantizeAndDequantizeV4(  # For your specific case
    tensor=quantize_input,                         # quantize_input
    scales=tensor.h,                               # Use the actual tensor.h with your case here
    zero_point=tensor.q,                           # Use the actual tensor.q with your case here
    inclusive_min=tensor.inclusive_min,
    inclusive_max=tensor.inclusive_max
)

# Now if quantize_input variable holds the eigth position in your tensor.
# And if image_heatmap holds your tensor holding values based on your accuracy giving locations.
image_heatmap = tf.nn.sigmoid(image_original_shape)
image_number = image_heatmap[quantize_input, :]

# Now you're ready to compute the gradients
with tf.GradientTape() as tape:
    gradient = tape.gradient(image_number, quantize_input)

