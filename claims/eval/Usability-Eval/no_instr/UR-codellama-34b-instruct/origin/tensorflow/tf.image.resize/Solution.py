
import tensorflow as tf

# Load the image
image = tf.io.read_file('image.jpg')

# Resize the image using bilinear interpolation
resized_image = tf.image.resize(image, (224, 224), method='bilinear')

# Display the resized image
display(resized_image)
