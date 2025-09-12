import tensorflow as tf

def resize_quantized_images(images, size):
    # Assuming the images are quantized in the range [0, 255]
    # We first dequantize the images
    images = tf.cast(images, tf.float32) / 255.0

    # Then we resize the images
    resized_images = tf.image.resize(images, size, method=tf.image.ResizeMethod.BILINEAR)

    # Finally, we quantize the resized images back to the range [0, 255]
    resized_images = tf.cast(resized_images * 255.0, tf.uint8)

    return resized_images
