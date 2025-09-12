import tensorflow as tf

def crop_and_resize_images(images, boxes, box_indices, crop_size):
    """
    Crop and resize regions of images.

    Arguments:
    images -- a 4D tensor of shape [batch, image_height, image_width, channels].
    boxes -- a 2D tensor of shape [num_boxes, 4]. The i-th row of the tensor specifies
              the coordinates of a box in the i-th image.
    box_indices -- a 1D tensor of length [num_boxes]. It specifies image indices
                   corresponding to each box.
    crop_size -- two element tuple specifying the size to which to crop and resize.

    Returns:
    A 4D tensor of shape [num_boxes, crop_height, crop_width, channels]
    """
    cropped_images = tf.image.crop_and_resize(images, boxes, box_indices, crop_size)

    return cropped_images
