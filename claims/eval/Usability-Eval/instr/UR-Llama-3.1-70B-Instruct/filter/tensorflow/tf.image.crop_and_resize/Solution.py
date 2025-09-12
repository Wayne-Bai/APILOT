
import tensorflow as tf

def extract_and_resize_crops(image, box_indices, crop_sizes):
    """
    Extracts crops from the input image tensor and resizes them.

    Args:
        image (tf.Tensor): Input image tensor with shape [height, width, channels].
        box_indices (tf.Tensor): 1D tensor of length 4, specifying the [y, x, height, width] of the crop box.
        crop_sizes (tf.Tensor): 1D tensor of length 2, specifying the target [height, width] of the resized crop.

    Returns:
        tf.Tensor: Resized crop tensor with shape [crop_height, crop_width, channels].
    """
    # Extract the crop from the input image using tf.slice
    y, x, height, width = tf.split(box_indices, num_or_size_splits=4)
    y = tf.cast(y, tf.int32)
    x = tf.cast(x, tf.int32)
    height = tf.cast(height, tf.int32)
    width = tf.cast(width, tf.int32)
    crop = tf.slice(image, [y, x, 0], [height, width, -1])

    # Resize the extracted crop using tf.image.resize
    resized_crop = tf.image.resize(crop, crop_sizes)
    return resized_crop

# Example usage:
if __name__ == "__main__":
    # Create a sample image tensor
    image = tf.random.normal(shape=[256, 256, 3])

    # Define the box indices and crop sizes
    box_indices = tf.constant([10, 10, 100, 100], dtype=tf.int32)
    crop_sizes = tf.constant([224, 224])

    # Extract and resize the crop
    resized_crop = extract_and_resize_crops(image, box_indices, crop_sizes)
    print(resized_crop.shape)
