import tensorflow as tf

# Load the input image
input_image = tf.io.read_file('input_image.jpg')

# Convert the input image to a TensorFlow tensor
input_tensor = tf.convert_to_tensor(input_image)

# Resize the input image to size (256, 256) using bicubic interpolation
resized_image = tf.image.resize(input_tensor, (256, 256), method='bicubic')

# Save the resized image to a file
tf.io.write_file('output_image.jpg', resized_image)
