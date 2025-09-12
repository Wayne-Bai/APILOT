
import tensorflow as tf

# Load the image using TensorFlow's io_util library
image_file = tf.io_util.read_file('path/to/image.jpg')

# Resize the image using the interpolation method specified
interpolation_method = 'bilinear' # or 'nearest'
resize_size = (224, 224)
image = tf.image.resize(image_file, resize_size, interpolation_method)
