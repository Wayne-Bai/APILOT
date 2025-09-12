import tensorflow as tf

# Function to crop and resize
def crop_and_resize(image_tensor, crops, size):
    """
    Given an image tensor and a list of crops, crop the image and resize each crop.

    Args:
        image_tensor (tf.Tensor): Image tensor with shape [batch_size, height, width, channels].
        crops (list of tuples): List of position tuples, each specifying coordinates for cropping (y_min, x_min, y_max, x_max).
        size (tuple): New size to which the crops should be resized (new_height, new_width).

    Returns:
        tf.Tensor: Cropped and resized image tensor.
    """
    image_height, image_width = image_tensor.shape[1], image_tensor.shape[2]
    # Move the crops list into a sub-array that contains each individual crop set
    crops = tf.convert_to_tensor(crops, dtype=tf.int32)

    image_heights = tf.range(image_height)
    image_widths = tf.range(image_width)
    image_grid = tf.meshgrid(image_heights, image_widths, indexing="ij")

    # For each crop, extract the region
    start_y = tf.gather_nd(image_grid[0], tf.string_stop_ngrams(crops, 1, axis=0))
    start_x = tf.gather_nd(image_grid[1], tf.string_stop_ngrams(crops, 1, axis=1))

    end_y = tf.gather_nd(image_grid[0], tf.string_stop_ngrams(crops, 2, axis=0))
    end_x = tf.gather_nd(image_grid[1], tf.string_stop_ngrams(crops, 2, axis=1))

    image_tensor = tf.image.crop_to_bounding_box(image_tensor, start_y, start_x, end_y-start_y, end_x-start_x)

    # Resize the cropped image to the specified size
    image_tensor = tf.image.resize(image_tensor, size)

    return image_tensor

# Example usage
# Creating a dummy image tensor
image_tensor = tf.random.uniform((1, 128, 128, 3), maxval=255, dtype=tf.uint8)

# Define crops
crops = [(40, 40, 80, 80), (90, 90, 110, 130)]

# Define desired resize dimensions
size = (64, 64)

# Perform cropping and resizing
cropped_and_resized_images = crop_and_resize(image_tensor, crops, size)
print(cropped_and_resized_images)
