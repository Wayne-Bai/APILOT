import tensorflow as tf

def resize_image(image, target_height, target_width, method='bilinear'):
    """
    Resize an image to the specified height and width using the specified method.

    Args:
    image (tf.Tensor): Input image tensor.
    target_height (int): Target height for the resized image.
    target_width (int): Target width for the resized image.
    method (str): Resizing method. Options include 'bilinear', 'nearest', 'bicubic', 'area', 'lanczos3',
                  'lanczos5', 'gaussian', 'mitchellcubic'.

    Returns:
    tf.Tensor: Resized image tensor.
    """
    # Convert method string to TensorFlow's ResizeMethod enum
    resize_method = {
        'bilinear': tf.image.ResizeMethod.BILINEAR,
        'nearest': tf.image.ResizeMethod.NEAREST_NEIGHBOR,
        'bicubic': tf.image.ResizeMethod.BICUBIC,
        'area': tf.image.ResizeMethod.AREA,
        'lanczos3': tf.image.ResizeMethod.LANCZOS3,
        'lanczos5': tf.image.ResizeMethod.LANCZOS5,
        'gaussian': tf.image.ResizeMethod.GAUSSIAN,
        'mitchellcubic': tf.image.ResizeMethod.MITCHELLCUBIC
    }[method]

    resized_image = tf.image.resize(image, [target_height, target_width], method=resize_method)
    return resized_image
