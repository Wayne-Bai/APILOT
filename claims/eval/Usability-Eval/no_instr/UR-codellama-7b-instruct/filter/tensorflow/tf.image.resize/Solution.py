
import tensorflow as tf

# Load the image
image = tf.io.read_file(filename)

# Convert the image to a tensor
image_tensor = tf.convert_to_tensor(image, dtype=tf.float32)

# Resize the image using tf.image.resize
resized_image = tf.image.resize(image_tensor, [new_width, new_height])

# Save the resized image
tf.io.write_file(resized_image, output_filename)
