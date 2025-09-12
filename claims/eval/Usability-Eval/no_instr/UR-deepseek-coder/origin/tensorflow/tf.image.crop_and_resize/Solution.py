import tensorflow as tf

def extract_and_resize_crops(image, crop_sizes, resize_size):
    """
    Extracts crops from the input image tensor and resizes them.

    Args:
    image: A 4D tensor of shape [batch, height, width, channels].
    crop_sizes: A list of tuples, each tuple representing the (height, width) of the crops to extract.
    resize_size: A tuple representing the (height, width) to resize the crops to.

    Returns:
    A list of resized crops.
    """
    crops = []
    for crop_size in crop_sizes:
        crop = tf.image.extract_patches(
            images=image,
            sizes=[1, crop_size[0], crop_size[1], 1],
            strides=[1, crop_size[0], crop_size[1], 1],
            rates=[1, 1, 1, 1],
            padding='VALID'
        )
        crop = tf.reshape(crop, [-1, crop_size[0], crop_size[1], image.shape[-1]])
        resized_crop = tf.image.resize(crop, resize_size)
        crops.append(resized_crop)
    return crops

# Example usage:
# Assuming 'input_image' is a 4D tensor of shape [batch, height, width, channels]
# crop_sizes = [(100, 100), (50, 50)]
# resize_size = (224, 224)
# resized_crops = extract_and_resize_crops(input_image, crop_sizes, resize_size)
