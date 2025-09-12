import tensorflow as tf

def resize_quantized_images(images, size, min_range, max_range):
    # Convert the images to float32 for resizing
    images_float = tf.cast(images, tf.float32)
    
    # Perform the resizing using bilinear interpolation
    resized_images_float = tf.image.resize(images_float, size, method=tf.image.ResizeMethod.BILINEAR)
    
    # Quantize the resized images back to the original range
    resized_images_quantized = tf.quantization.fake_quant_with_min_max_args(
        resized_images_float, min_range, max_range, num_bits=8, narrow_range=False
    )
    
    return resized_images_quantized

# Example usage:
# images = ...  # Your quantized image tensor with shape [batch, height, width, channels]
# size = [new_height, new_width]  # Desired output size
# min_range = ...  # Minimum value of the quantization range
# max_range = ...  # Maximum value of the quantization range

# resized_images = resize_quantized_images(images, size, min_range, max_range)
