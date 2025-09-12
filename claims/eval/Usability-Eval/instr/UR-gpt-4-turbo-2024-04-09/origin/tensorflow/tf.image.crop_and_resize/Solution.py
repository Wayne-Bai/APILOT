import tensorflow as tf

def extract_and_resize_images(input_tensor, boxes, crop_size):
    """
    Extracts crops from the input image tensor and resizes them using the new 'tf.image.crop_and_resize' function.
    
    Args:
    input_tensor (tf.Tensor): A batch of images tensor of shape (batch_size, height, width, channels).
    boxes (List[List[float]]): A list of boxes, each box specified by [y1, x1, y2, x2] in normalized coordinates.
    crop_size (List[int]): A two-element list [crop_height, crop_width], the size of the output crops.

    Returns:
    tf.Tensor: A tensor containing the resized crops from the input image tensor.
    """
    box_indices = tf.range(start=0, limit=tf.shape(input_tensor)[0], dtype=tf.int32)
    cropped_images = tf.image.crop_and_resize(input_tensor, boxes, box_indices, crop_size)
    return cropped_images
