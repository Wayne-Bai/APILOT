import tensorflow as tf

def extract_and_resize_images(input_tensor, boxes, crop_size):
    """
    Extracts crops from the input image tensor and resizes them using TensorFlow.

    Parameters:
    - input_tensor (tf.Tensor): 4-D Tensor of shape [batch, height, width, channels].
    - boxes (tf.Tensor): 2-D Tensor of shape [num_boxes, 4] containing normalized coordinates [y1, x1, y2, x2].
    - crop_size (List[int, int]): The size to resize the extracted crop [new_height, new_width].

    Returns:
    - tf.Tensor: A 4-D tensor with the resized crops.
    """
    # Use `tf.image.crop_and_resize` for cropping and resizing images
    box_indices = tf.range(tf.shape(boxes)[0])
    crops = tf.image.crop_and_resize(input_tensor, boxes, box_indices, crop_size)
    return crops
