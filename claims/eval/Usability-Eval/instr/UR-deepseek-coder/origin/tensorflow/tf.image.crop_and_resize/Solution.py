import tensorflow as tf

def extract_and_resize_crops(image, crop_sizes, resize_size):
    """
    Extracts crops from the input image tensor and resizes them.

    Args:
    image: A 4D tensor of shape [batch, height, width, channels].
    crop_sizes: A list of tuples, each tuple representing the (height, width) of the crops to extract.
    resize_size: A tuple (height, width) representing the size to resize the crops to.

    Returns:
    A list of resized crops.
    """
    crops = []
    for crop_size in crop_sizes:
        crop = tf.image.random_crop(image, [image.shape[0], crop_size[0], crop_size[1], image.shape[3]])
        resized_crop = tf.image.resize(crop, resize_size, method=tf.image.ResizeMethod.BILINEAR)
        crops.append(resized_crop)
    return crops

# Example usage:
# Assuming `input_image` is a 4D tensor of shape [batch, height, width, channels]
# crop_sizes = [(100, 100), (150, 150)]
# resize_size = (50, 50)
# resized_crops = extract_and_resize_crops(input_image, crop_sizes, resize_size)
