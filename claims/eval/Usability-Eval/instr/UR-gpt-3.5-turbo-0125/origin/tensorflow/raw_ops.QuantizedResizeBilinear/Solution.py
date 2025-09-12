
import tensorflow as tf

def resize_quantized_images(input_images, size):
    return tf.image.resize(input_images, size, method=tf.image.ResizeMethod.BILINEAR, preserve_aspect_ratio=False)

# Using the created function
input_images = tf.placeholder(tf.uint8, [None, None, None, None])
output_images = resize_quantized_images(input_images, [500, 500])
