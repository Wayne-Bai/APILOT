import tensorflow as tf

def resize_quantized_images(images, size, method=tf.image.ResizeMethod.BILINEAR):
    # Quantize the images
    quantized_images = tf.quantization.quantize_via_process(images)

    # Resize the quantized images using quantized bilinear interpolation
    resized_images = tf.image.resize(quantized_images, size, method=method)

    return resized_images
