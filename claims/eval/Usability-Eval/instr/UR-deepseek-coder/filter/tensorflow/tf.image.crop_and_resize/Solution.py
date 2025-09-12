import tensorflow as tf

def extract_and_resize_crops(image, crop_sizes, resize_size):
    """
    Extracts crops from the input image tensor and resizes them.

    Args:
    image: A 4D tensor of shape [batch, height, width, channels].
    crop_sizes: A list of tuples, where each tuple is (height, width) of the crop.
    resize_size: A tuple (height, width) specifying the size to resize the crops.

    Returns:
    A list of resized crops.
    """
    crops = []
    for size in crop_sizes:
        crop = tf.image.extract_patches(
            images=image,
            sizes=[1, size[0], size[1], 1],
            strides=[1, size[0], size[1], 1],
            rates=[1, 1, 1, 1],
            padding='VALID'
        )
        crop = tf.reshape(crop, [-1, size[0], size[1], image.shape[-1]])
        resized_crop = tf.image.resize(crop, resize_size)
        crops.append(resized_crop)
    return crops

# Example usage:
# image = ...  # Your 4D image tensor
# crop_sizes = [(64, 64), (128, 128)]
# resize_size = (32, 32)
# resized_crops = extract_and_resize_crops(image, crop_sizes, resize_size)
