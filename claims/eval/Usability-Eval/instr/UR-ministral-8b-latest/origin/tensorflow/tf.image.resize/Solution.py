import tensorflow as tf

def resize_image(image, size):
    # Use TensorFlow's resize function to rescale the image
    resized_image = tf.image.resize(image, size)

    return resized_image
