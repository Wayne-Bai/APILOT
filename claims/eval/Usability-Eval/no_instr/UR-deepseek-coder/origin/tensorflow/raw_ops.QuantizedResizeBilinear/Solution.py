import tensorflow as tf

def resize_quantized_images(images, size, min_range, max_range):
    # Convert the quantized images to float for resizing
    images_float = tf.cast(images, tf.float32)
    
    # Resize the images using bilinear interpolation
    resized_images_float = tf.image.resize(images_float, size, method=tf.image.ResizeMethod.BILINEAR)
    
    # Quantize the resized images back to the original range
    resized_images_quantized = tf.quantization.quantize_and_dequantize_v2(
        resized_images_float,
        input_min=min_range,
        input_max=max_range,
        range_given=True,
        signed_input=False
    )
    
    return resized_images_quantized

# Example usage:
# images: Tensor of shape [batch, height, width, channels]
# size: Tuple of new height and width (new_height, new_width)
# min_range, max_range: The quantization range of the input images
images = tf.constant([...])  # Replace with your actual image data
size = (new_height, new_width)  # Replace with your desired size
min_range = 0.0  # Replace with your actual min range
max_range = 255.0  # Replace with your actual max range

resized_images = resize_quantized_images(images, size, min_range, max_range)
