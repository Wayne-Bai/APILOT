import tensorflow as tf

# Assuming you have a quantized image tensor 'image' with shape (height, width, channels)
# and you want to resize it to a new size (new_height, new_width)

# Calculate the scale factors for height and width
scale_height = tf.cast(new_height, tf.float32) / tf.cast(height, tf.float32)
scale_width = tf.cast(new_width, tf.float32) / tf.cast(width, tf.float32)

# Perform the quantized bilinear interpolation
resized_image = tf.image.resize(image, (new_height, new_width), method=tf.image.ResizeMethod.BILINEAR)
resized_image = tf.round(resized_image)

# Quantize the resized image to the original quantization levels
quantized_image = tf.quantization.quantize_via_dequantization(resized_image)

# Scale the quantized image to the new size
quantized_image = tf.image.resize(quantized_image, (new_height, new_width), method=tf.image.ResizeMethod.NEAREST_NEIGHBOR)

# Dequantize the resized image
resized_image = tf.quantization.dequantize(quantized_image)
