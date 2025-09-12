import tensorflow as tf

def resize_quantized_images(images, size):
    # Perform dequantization
    dequantized_images = tf.cast(images, tf.float32) / 255.0

    # Resize dequantized images
    resized_images = tf.image.resize(dequantized_images, size)

    # Perform quantization
    quantized_images = tf.cast(resized_images * 255.0, tf.uint8)

    return quantized_images
