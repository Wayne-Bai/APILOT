import tensorflow as tf

def extract_and_resize_crops(image, boxes, crop_size):
    """
    Extracts crops from the input image tensor and resizes them.

    Args:
    image: A 4-D float Tensor of shape [batch, height, width, channels] containing the input image.
    boxes: A 2-D float Tensor of shape [num_boxes, 4] containing the bounding boxes in the format [y_min, x_min, y_max, x_max].
    crop_size: A tuple of two integers (height, width) specifying the desired output size of the crops.

    Returns:
    A 4-D float Tensor of shape [batch, num_boxes, crop_size[0], crop_size[1], channels] containing the resized crops.
    """
    # Calculate the coordinates of the crops
    y_mins = boxes[:, 0]
    x_mins = boxes[:, 1]
    y_maxs = boxes[:, 2]
    x_maxs = boxes[:, 3]

    # Calculate the coordinates of the top-left and bottom-right corners of the crops
    top_left_ys = tf.maximum(0, y_mins)
    top_left_xs = tf.maximum(0, x_mins)
    bottom_right_ys = tf.minimum(tf.shape(image)[1], y_maxs)
    bottom_right_xs = tf.minimum(tf.shape(image)[2], x_maxs)

    # Extract the crops from the input image
    crops = tf.image.crop_to_bounding_box(image, top_left_ys, top_left_xs, bottom_right_ys - top_left_ys, bottom_right_xs - top_left_xs)

    # Resize the crops to the desired output size
    resized_crops = tf.image.resize(crops, crop_size)

    return resized_crops
