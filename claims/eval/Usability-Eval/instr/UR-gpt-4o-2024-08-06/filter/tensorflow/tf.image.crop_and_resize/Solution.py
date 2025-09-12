import tensorflow as tf

def extract_and_resize(image, boxes, target_height, target_width):
    """
    Extracts crops from the input image tensor and resizes them.

    Parameters:
    - image: Tensor, input image of shape (height, width, channels).
    - boxes: Tensor, shape (num_boxes, 4) containing the normalized coordinates of the boxes 
              to be used for cropping. Each box is specified by its normalized [y1, x1, y2, x2] coordinates.
    - target_height: int, the height of the output crops.
    - target_width: int, the width of the output crops.

    Returns:
    - Resized crops, a 4D tensor of shape (num_boxes, target_height, target_width, channels).
    """
    # Ensure the boxes are in the form of 2D tensor with each box as [y1, x1, y2, x2]
    if not (isinstance(boxes, tf.Tensor) and boxes.shape[1] == 4):
        raise ValueError("boxes should be a tensor with shape (num_boxes, 4)")
    
    # Extracting crop_and_resize using the updated tf.image API method.
    crops = tf.image.crop_and_resize(
        image=tf.expand_dims(image, axis=0),  # making image 4D as required
        boxes=boxes,
        box_indices=tf.range(tf.shape(boxes)[0]),
        crop_size=[target_height, target_width]
    )
    
    return crops
