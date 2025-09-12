import tensorflow as tf

# Create a function to resize quantized images using bilinear interpolation
def resize_quantized_images(input_image, input_min, input_max, target_size):
    """
    Resize quantized images to a target size using bilinear interpolation.

    Parameters:
    input_image: A quantized tensor representing the image to be resized
    input_min: The minimum value of the quantized input image
    input_max: The maximum value of the quantized input image
    target_size: A tuple (height, width) representing the target size

    Returns:
    Resized quantized image tensor and the new range [new_min, new_max].
    """
    
    # First dequantize the image to float32 for processing
    float_image = tf.quantization.dequantize(input_image, input_min, input_max)

    # Resize using bilinear interpolation
    resized_float_image = tf.image.resize(float_image, target_size, method='bilinear')

    # Optionally determine new min/max if necessary
    # This code assumes the range needs to be directly recalculated
    new_min = tf.reduce_min(resized_float_image)
    new_max = tf.reduce_max(resized_float_image)

    # Quantize back to previous range; adjust range if necessary
    resized_quantized_image = tf.quantization.quantize(resized_float_image, new_min, new_max, T=tf.quint8)

    return resized_quantized_image.output, resized_quantized_image.output_min, resized_quantized_image.output_max

# Example usage:
# Assume 'image_quantized' is a quantized image tensor with its min/max values
# target_size is a tuple (new_height, new_width)
image_quantized = tf.constant([[0, 255], [128, 64]], dtype=tf.quint8)
min_val, max_val = 0.0, 255.0  # Example min/max values of the quantized image
target_size = (100, 100)  # New size

# Call the resize function
resized_image, new_min, new_max = resize_quantized_images(image_quantized, min_val, max_val, target_size)

# Print the resized image and its new range
print(resized_image)
print("New min:", new_min.numpy())
print("New max:", new_max.numpy())
