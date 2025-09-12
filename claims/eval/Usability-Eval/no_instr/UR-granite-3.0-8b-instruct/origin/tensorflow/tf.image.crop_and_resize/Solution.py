import tensorflow as tf

def extract_and_resize_crops(image, boxes, output_size):
    """
    Extracts crops from the input image tensor and resizes them.

    Args:
    image (tf.Tensor): The input image tensor of shape (height, width, channels).
    boxes (tf.Tensor): The bounding boxes tensor of shape (num_boxes, 4), where each row is (x_min, y_min, x_max, y_max).
    output_size (tuple): The desired output size of the crops as a tuple (height, width).

    Returns:
    tf.Tensor: The resized crops tensor of shape (num_boxes, height, width, channels).
    """
    # Convert boxes to corner form
    boxes = tf.concat([boxes[:, :2] - boxes[:, 2:] / 2, boxes[:, :2] + boxes[:, 2:] / 2], axis=-1)

    # Extract crops
    crops = tf.image.crop_to_bounding_box(image, boxes[:, 0], boxes[:, 1], boxes[:, 2] - boxes[:, 0], boxes[:, 3] - boxes[:, 1])

    # Resize crops
    crops = tf.image.resize(crops, output_size, method=tf.image.ResizeMethod.BILINEAR)

    return crops
