import tensorflow as tf

def resize_quantized_image(input_image, output_height, output_width, min_val, max_val):
    # Convert quantized input to float for processing
    input_image_float = tf.cast(input_image, tf.float32)

    # Normalize the image to the range [0, 1]
    normalized_image = (input_image_float - min_val) / (max_val - min_val)

    # Use resize method available in tf.image using bilinear interpolation
    resized_image_float = tf.image.resize(
        normalized_image, [output_height, output_width], method=tf.image.ResizeMethod.BILINEAR)

    # Rescale back to the original quantized range and cast back to desired dtype
    resized_image = tf.cast(resized_image_float * (max_val - min_val) + min_val, input_image.dtype)

    return resized_image

# Example Usage
if __name__ == "__main__":
    # Example quantized image
    quantized_image = tf.constant([[1, 2], [3, 4]], dtype=tf.uint8)
    min_val_example, max_val_example = 0, 255  # Example min and max values for uint8

    # Resize parameters
    new_height, new_width = 4, 4

    # Resize the quantized image
    resized_quantized_image = resize_quantized_image(
        quantized_image, new_height, new_width, min_val_example, max_val_example)

    print("Resized Quantized Image:\n", resized_quantized_image.numpy())
