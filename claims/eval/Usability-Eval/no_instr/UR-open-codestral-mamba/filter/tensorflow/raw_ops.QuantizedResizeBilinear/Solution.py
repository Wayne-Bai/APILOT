import tensorflow as tf

def resize_quantized_images(images, size):
    # Create a QuantizeV2 layer
    quantize = tf.raw_ops.QuantizeV2(input=images, T=tf.uint8, min_range=tf.constant(0.0, dtype=tf.float32), max_range=tf.constant(255.0, dtype=tf.float32))

    # Use tf.image.resize to resize the images using bilinear interpolation
    resized_quantized = tf.image.resize(quantized, size, method=tf.image.ResizeMethod.BILINEAR)

    # Dequantize the resized images
    dequantize = tf.raw_ops.Dequantize(input=resized_quantized, T=tf.uint8, min_range=tf.constant(0.0, dtype=tf.float32), max_range=tf.constant(255.0, dtype=tf.float32))

    return dequantize
