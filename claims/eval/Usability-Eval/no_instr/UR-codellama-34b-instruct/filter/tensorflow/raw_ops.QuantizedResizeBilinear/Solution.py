import tensorflow as tf

# Load the image data
image = tf.io.read_file('path/to/image.jpg')

# Decode the image data
decoded_image = tf.image.decode_jpeg(image)

# Resize the decoded image using quantized bilinear interpolation
resized_image = tf.raw_ops.resize_quantized_images(
    input=decoded_image,
    size=[new_height, new_width],
    method='bilinear',
    preserve_aspect_ratio=False)

# Save the resized image to a file
tf.io.write_file('path/to/resized_image.jpg', resized_image)
