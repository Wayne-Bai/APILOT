# Import the necessary libraries
import tensorflow as tf

# Define the function to draw bounding boxes
def draw_bounding_boxes(images, boxes, colors):
    """
    Draw bounding boxes on a batch of images.

    Args:
        images (tf.Tensor): A tensor of shape [batch_size, height, width, channels] representing the images.
        boxes (tf.Tensor): A tensor of shape [batch_size, num_boxes, 4] representing the bounding boxes.
        colors (tf.Tensor): A tensor of shape [num_boxes, 3] representing the colors of the bounding boxes.

    Returns:
        tf.Tensor: A tensor of shape [batch_size, height, width, channels] representing the images with bounding boxes drawn.
    """
    # Ensure the input tensors have the correct shapes
    images = tf.ensure_shape(images, [None, None, None, 3])
    boxes = tf.ensure_shape(boxes, [None, None, 4])
    colors = tf.ensure_shape(colors, [None, 3])

    # Draw the bounding boxes
    output = tf.raw_ops.DrawBoundingBoxes(
        images=images,
        boxes=boxes,
        colors=colors
    )

    return output

# Example usage
if __name__ == "__main__":
    # Create a batch of images
    images = tf.random.uniform(shape=[2, 256, 256, 3], minval=0, maxval=255, dtype=tf.int32)

    # Define the bounding boxes
    boxes = tf.constant([
        [[0.1, 0.1, 0.5, 0.5], [0.6, 0.6, 0.9, 0.9]],
        [[0.2, 0.2, 0.6, 0.6], [0.7, 0.7, 0.95, 0.95]]
    ])

    # Define the colors
    colors = tf.constant([
        [255, 0, 0],
        [0, 0, 255]
    ])

    # Draw the bounding boxes
    output = draw_bounding_boxes(images, boxes, colors)

    print(output.shape)
