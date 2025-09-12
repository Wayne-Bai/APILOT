import tensorflow as tf

def resize_image(image, target_size, method='bilinear'):
    """
    Resizes the given image to the target size using the specified method.

    :param image: The input image tensor.
    :param target_size: A tuple of the desired (height, width).
    :param method: The method for resizing. Options include 'bilinear', 'nearest', 
                   'bicubic', 'lanczos3', 'lanczos5', 'gaussian', 'mitchellcubic'.
    :return: The resized image tensor.
    """
    methods = {
        'bilinear': tf.image.ResizeMethod.BILINEAR,
        'nearest': tf.image.ResizeMethod.NEAREST_NEIGHBOR,
        'bicubic': tf.image.ResizeMethod.BICUBIC,
        'lanczos3': tf.image.ResizeMethod.LANCZOS3,
        'lanczos5': tf.image.ResizeMethod.LANCZOS5,
        'gaussian': tf.image.ResizeMethod.GAUSSIAN,
        'mitchellcubic': tf.image.ResizeMethod.MITCHELLCUBIC
    }

    if method not in methods:
        raise ValueError(f"Method {method} is not recognised. Valid options are: {list(methods.keys())}")

    resized_image = tf.image.resize(image, target_size, method=methods[method])
    return resized_image

# Example Usage
# Assuming you have an image tensor `img_tensor` with shape [height, width, channels]
# target_size = (128, 128)
# resized_img = resize_image(img_tensor, target_size, method='bicubic')
