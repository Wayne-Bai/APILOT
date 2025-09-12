import tensorflow as tf

# Function to draw bounding boxes
def draw_bounding_boxes(images, boxes, colors=None):
    """
    Draws bounding boxes on a batch of images.
    
    Args:
        images: A 4-D tensor of shape `[batch, height, width, channels]` representing the input images.
        boxes: A 3-D tensor of shape `[batch, num_boxes, 4]` containing the bounding box coordinates.
               The coordinates are in normalized format (i.e., between 0 and 1)
               and correspond to `[y_min, x_min, y_max, x_max]`.
        colors: Optional. A 2-D tensor of shape `[num_boxes, 3]` specifying the RGB color for each box.
                If None, uses a default color.
                
    Returns:
        A 4-D tensor of the same shape as input images with bounding boxes drawn on them.
    """

    # Number of images in the batch
    batch_size = tf.shape(images)[0]
    
    if colors is None:
        # Create a default color map for the boxes if not specified
        colors = tf.constant([[1.0, 0.0, 0.0] for _ in range(tf.shape(boxes)[1])], dtype=tf.float32)  # Red color by default

    # Ensure colors are the right shape [num_boxes, channels]
    colors = tf.broadcast_to(colors, [tf.shape(boxes)[1], 3])
    
    # Draw bounding boxes on the batch of images
    images_with_boxes = tf.image.draw_bounding_boxes(images, boxes, colors)

    return images_with_boxes

# Example Usage
if __name__ == "__main__":
    # Sample input data
    batch_size = 2
    height, width, channels = 256, 256, 3
    num_boxes = 2

    # Random images
    images = tf.random.uniform([batch_size, height, width, channels], minval=0, maxval=1, dtype=tf.float32)

    # Random boxes (in normalized form)
    boxes = tf.random.uniform([batch_size, num_boxes, 4], minval=0, maxval=1, dtype=tf.float32)

    # Colors (optional)
    colors = tf.constant([[0.0, 1.0, 0.0], [0.0, 0.0, 1.0]], dtype=tf.float32)  # Green and Blue

    # Draw boxes on images
    images_with_boxes = draw_bounding_boxes(images, boxes, colors)

    # Depending on the environment, you may want to visualize the images_with_boxes
    # using other libraries like matplotlib to verify the results.
