
import tensorflow as tf

# Load the image file
image = tf.io.read_file('image.jpg')

# Decode the image data
image = tf.io.decode_jpeg(image)

# Resize the image using bilinear interpolation
resized_image = tf.image.resize(image, (640, 480), method='bilinear')

# Save the resized image to a new file
tf.io.write_file('resized_image.jpg', resized_image)
