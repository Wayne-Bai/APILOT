import tensorflow as tf

def resize_quantized_image(image, size):
    # Convert image to float32 to ensure compatibility with tensorflow operations
    image_float = tf.cast(image, tf.float32)

    # Define the required size for resizing
    height, width = size

    # Perform bilinear interpolation
    resized_image = tf.image.resize(image_float, [height, width], method=tf.image.ResizeMethod.BILINEAR)

    # Cast the resized image back to int8 for quantization
    resized_quantized_image = tf.cast(resized_image, tf.int8)

    return resized_quantized_image

# Example usage
input_image = tf.constant([[[[1, 2], [3, 4]]]], dtype=tf.int8)  # Assuming a small quantized image
resized_image = resize_quantized_image(input_image, (2, 2))  # Resize to a 2x2 image

print(resized_image)  # Show the resulting resized image
