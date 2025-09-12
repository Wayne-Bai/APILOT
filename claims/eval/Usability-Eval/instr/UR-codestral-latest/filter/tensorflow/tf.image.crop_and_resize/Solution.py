import tensorflow as tf

def crop_and_resize(image, boxes, box_indices, crop_size):
    """
    Crops and resizes regions from the image tensor.

    Args:
    image: A 4-D tensor of shape [batch, image_height, image_width, depth].
    boxes: A list of 2-D Tensors of shape [num_boxes, 4]. The i-th entry is a
           normalized coordinate for the region to crop from the image. Each
           coordinate should be between [0, 1]. eg: [y1, x1, y2, x2] where (y1,
           x1) and (y2, x2) are the coordinates of any diagonal pair of box corners.
    box_indices: A 1-D tensor of shape [num_boxes] with int32 values in [0, batch).
    crop_size: A list of two integers. The size to which the cropped image
               should be resized to. e.g., [height, width].

    Returns:
    A 4-D tensor of shape [num_boxes, crop_size[0], crop_size[1], depth]
    representing the cropped regions.
    """
    crops = tf.image.crop_and_resize(image, boxes, box_indices, crop_size)
    return crops
