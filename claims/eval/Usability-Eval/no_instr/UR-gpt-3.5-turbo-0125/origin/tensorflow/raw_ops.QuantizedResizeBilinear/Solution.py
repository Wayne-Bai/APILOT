
import tensorflow as tf

def resize_quantized_image(images, size, min_range, max_range):
    resized_images = tf.raw_ops.ResizeQuantizedBilinear(
        images=images,
        size=size,
        min_range=min_range,
        max_range=max_range
    )
    return resized_images
