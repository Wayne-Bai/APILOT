import tensorflow as tf

def resize_quantized_images(image, size):
    """
    Resize quantized images to size using quantized bilinear interpolation.

    Args:
        image: A tensor of type tf.int32 and rank 4.
        size: A 1-D tensor of 2 elements, size = [new_height, new_width].

    Returns:
        A resized 4-D tensor of type tf.int32.
    """

    # Ensure the input image and size are of the correct types and ranks
    image = tf.convert_to_tensor(image, dtype=tf.int32)
    size = tf.convert_to_tensor(size, dtype=tf.int32)
    size = tf.reshape(size, [2])

    # Check if the rank of the image tensor is 4
    if len(image.shape)!= 4:
        raise ValueError("Image should be a 4-D tensor")

    # Check if the size tensor is of rank 1 and has 2 elements
    if len(size.shape)!= 1 or size.shape[0]!= 2:
        raise ValueError("Size should be a 1-D tensor of 2 elements")

    # Use tf.raw_ops.ResizeNearestNeighbor to perform quantized bilinear interpolation
    size = tf.cast(size, tf.int32)
    image = tf.raw_ops.ResizeBilinear(
        images=image,
        size=size,
        align_corners=False,
        half_pixel_centers=False)

    return image


# Example usage
image = tf.random.normal(shape=[1, 256, 256, 3], dtype=tf.int32)
new_size = tf.constant([512, 512])
resized_image = resize_quantized_images(image, new_size)

print(resized_image.shape)
