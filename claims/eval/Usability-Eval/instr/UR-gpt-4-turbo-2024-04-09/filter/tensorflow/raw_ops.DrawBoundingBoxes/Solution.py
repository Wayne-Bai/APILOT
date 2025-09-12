import tensorflow as tf

def draw_bounding_boxes(images, boxes):
    """
    Draw bounding boxes on a batch of images.

    Args:
    images (tf.Tensor): A 4-D tensor of shape [batch, height, width, channels].
    boxes (tf.Tensor): A 3-D tensor of shape [batch, num_boxes, 4] representing the coordinates of the bounding boxes.
                       Each box is normalized [y_min, x_min, y_max, x_max] format.

    Returns:
    tf.Tensor: A 4-D tensor of the same type as `images`, with boxes drawn on them.
    """
    return tf.image.draw_bounding_boxes(images, boxes)

# Example usage:
# Suppose `input_images` is a batch of images with shape [batch_size, height, width, channels]
# And `input_boxes` is the corresponding bounding boxes with shape [batch_size, num_boxes, 4]
# where each box is normalized [y_min, x_min, y_max, x_max].
# Example values for demonstration (ensure your actual data conforms to expected dimensions and values)
input_images = tf.random.uniform(shape=[2, 256, 256, 3], minval=0, maxval=1)
input_boxes = tf.constant([[[0.1, 0.2, 0.5, 0.8], [0.15, 0.1, 0.4, 0.4]],
                           [[0.3, 0.3, 0.6, 0.6], [0.2, 0.4, 0.5, 0.75]]], dtype=tf.float32)

output_images = draw_bounding_boxes(input_images, input_boxes)

# Note: Visualizing or saving the output images would require additional steps not covered here.
