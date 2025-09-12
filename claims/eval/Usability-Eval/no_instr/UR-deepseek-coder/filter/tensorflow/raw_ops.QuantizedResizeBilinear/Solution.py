import tensorflow as tf

def resize_quantized_images(images, size, min_range, max_range):
    # Convert the quantized images to float for resizing
    images_float = tf.cast(images, tf.float32)
    
    # Resize the images using bilinear interpolation
    resized_images = tf.image.resize(images_float, size, method=tf.image.ResizeMethod.BILINEAR)
    
    # Quantize the resized images back to the original range
    quantized_resized_images = tf.quantization.quantize_and_dequantize_v2(
        resized_images,
        input_min=min_range,
        input_max=max_range,
        output_min=min_range,
        output_max=max_range,
        range_given=True
    )
    
    return quantized_resized_images

# Example usage:
# images: Tensor of shape [batch, height, width, channels]
# size: Tuple of new height and width (new_height, new_width)
# min_range, max_range: The range of the input quantized images

# Assuming images is a Tensor of shape [batch, height, width, channels]
# and size is a tuple (new_height, new_width)
# min_range and max_range are the quantization ranges

resized_quantized_images = resize_quantized_images(images, size, min_range, max_range)
