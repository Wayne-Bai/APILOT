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
    for crop_size in crop_sizes:
        crop = tf.image.random_crop(image, [tf.shape(image)[0], crop_size[0], crop_size[1], tf.shape(image)[-1]])
        resized_crop = tf.image.resize(crop, resize_size, method=tf.image.ResizeMethod.BILINEAR)
        crops.append(resized_crop)
    return crops

# Example usage:
# image = ...  # Your 4D image tensor
# crop_sizes = [(100, 100), (150, 150)]
# resize_size = (200, 200)
# resized_crops = extract_and_resize_crops(image, crop_sizes, resize_size)
