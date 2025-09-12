import tensorflow as tf

def extract_and_resize_images(input_tensor, boxes, crop_size):
    """
    Extracts crops from the input image tensor and resizes them using TensorFlow.

    Parameters:
    - input_tensor: A 4-D tensor of shape `[batch, height, width, channels]`.
    - boxes: A 2-D tensor of shape `[num_boxes, 4]` containing the normalized
             coordinates of the boxes in the format `[y1, x1, y2, x2]`.
    - crop_size: A tuple or list of two integers specifying the new size to which
                 each crop is resized (height, width).

    Returns:
    - A 4-D tensor containing the resized crops.
    """

    box_indices = tf.range(tf.shape(boxes)[0])
    crops = tf.image.crop_and_resize(image=input_tensor, boxes=boxes, box_indices=box_indices, crop_size=crop_size)
    return crops
