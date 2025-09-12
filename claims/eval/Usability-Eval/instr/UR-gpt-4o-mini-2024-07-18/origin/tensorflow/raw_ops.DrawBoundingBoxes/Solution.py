import tensorflow as tf

def draw_bounding_boxes_on_images(images, boxes, colors=[[1, 0, 0]], line_thickness=2):
    """
    Draw bounding boxes on a batch of images.

    Args:
        images: A 4-D tensor of shape [batch, height, width, channels].
        boxes: A 3-D tensor of shape [batch, N, 4] where N is the number of bounding boxes,
               and each box is represented as [y_min, x_min, y_max, x_max].
        colors: A list of colors for the bounding boxes. Each color is a list of 3 float values.
        line_thickness: The thickness of the bounding box lines.

    Returns:
        A 4-D tensor of the images with bounding boxes drawn on them.
    """
    
    # Ensure the right shape of input images and boxes
    batch_size = tf.shape(images)[0]
    
    # Draw bounding boxes using tf.image.draw_bounding_boxes
    images_with_boxes = tf.image.draw_bounding_boxes(images, boxes[:, :, tf.newaxis, :], colors=colors)
    
    return images_with_boxes

# Example usage
# Assuming images is a tensor of shape [batch_size, height, width, channels]
# and boxes is a tensor of shape [batch_size, N, 4]
# images = ...
# boxes = ...
# images_with_bboxes = draw_bounding_boxes_on_images(images, boxes)
