import tensorflow as tf

def resize_image(image, target_size, method='bilinear'):
    """
    Resizes an image to the specified size using the specified method.

    Parameters:
    - image: the original image tensor.
    - target_size: tuple (height, width) for resizing.
    - method: the interpolation method. Options include:
      'bilinear', 'nearest', 'bicubic', 'area', 'lanczos3', 'lanczos5',
      'gaussian', 'mitchellcubic'.

    Returns:
    - Resized image tensor.
    """

    # Map string to respective tf.image.ResizeMethod
    method_map = {
        'bilinear': tf.image.ResizeMethod.BILINEAR,
        'nearest': tf.image.ResizeMethod.NEAREST_NEIGHBOR,
        'bicubic': tf.image.ResizeMethod.BICUBIC,
        'area': tf.image.ResizeMethod.AREA,
        'lanczos3': tf.image.ResizeMethod.LANCZOS3,
        'lanczos5': tf.image.ResizeMethod.LANCZOS5,
        'gaussian': tf.image.ResizeMethod.GAUSSIAN,
        'mitchellcubic': tf.image.ResizeMethod.MITCHELLCUBIC
    }

    # Select the interpolation method
    interpolation_method = method_map.get(method.lower(), tf.image.ResizeMethod.BILINEAR)

    # Resize the image
    resized_image = tf.image.resize(
        images=image,
        size=target_size,
        method=interpolation_method
    )

    return resized_image

# Example usage:
# Suppose 'raw_image_tensor' is a tensor representing an image with shape [height, width, channels]
# You might get it using tf.io.decode_image on JPEG/PNG files for instance.

# raw_image_tensor = ... # Load your image tensor
# resized_image = resize_image(raw_image_tensor, target_size=(200, 300), method='bicubic')

# The resized_image will have the shape (200, 300, channels)

