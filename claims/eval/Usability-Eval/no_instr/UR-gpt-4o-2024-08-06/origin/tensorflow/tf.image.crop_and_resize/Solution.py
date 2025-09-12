import tensorflow as tf

def extract_and_resize_crops(image, boxes, crop_size):
    """
    Extracts crops from the input image tensor and resizes them.

    Parameters:
        image (tf.Tensor): A 3-D tensor of shape [height, width, channels] containing the input image.
        boxes (tf.Tensor): A 2-D tensor of shape [num_boxes, 4] containing the normalized coordinates of
                           boxes as [y1, x1, y2, x2].
        crop_size (tuple): A tuple specifying the desired output size of each crop as (crop_height, crop_width).

    Returns:
        tf.Tensor: A 4-D tensor containing the extracted and resized crops of shape [num_boxes, crop_height, crop_width, channels].
    """
    # Expand dimensions to add batch size
    image = tf.expand_dims(image, axis=0)

    # Get crops
    crops = tf.image.crop_and_resize(image, boxes, box_indices=tf.zeros([tf.shape(boxes)[0]], dtype=tf.int32), crop_size=crop_size)

    return crops

# Example usage
image = tf.random.uniform((256, 256, 3))  # Example image tensor
boxes = tf.constant([[0.1, 0.1, 0.5, 0.5], [0.5, 0.5, 0.9, 0.9]])  # Example boxes
crop_size = (64, 64)  # Desired output size

crops = extract_and_resize_crops(image, boxes, crop_size)
print(crops.shape)  # Output: (2, 64, 64, 3)
