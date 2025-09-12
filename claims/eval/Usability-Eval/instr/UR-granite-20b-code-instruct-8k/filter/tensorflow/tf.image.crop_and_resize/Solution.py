import tensorflow as tf

# Assuming image is a tensor of shape [height, width, channels]
cropped_images = tf.image.resize(images, size=[128, 128])
