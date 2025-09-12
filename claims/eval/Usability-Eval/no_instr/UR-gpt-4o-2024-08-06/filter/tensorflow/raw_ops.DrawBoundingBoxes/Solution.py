import tensorflow as tf

def draw_bounding_boxes(images, boxes, colors):
    """
    Draw bounding boxes on a batch of images.

    Parameters:
    images: Tensor of shape [batch_size, height, width, channels]. The batch of images to draw on.
    boxes: Tensor of shape [batch_size, num_boxes, 4]. Each box is represented as [y_min, x_min, y_max, x_max].
    colors: Tensor of shape [batch_size, num_boxes, 3]. Colors for each box.

    Returns:
    A tensor of images with bounding boxes drawn on them.
    """
    batch_size = tf.shape(images)[0]
    num_boxes = tf.shape(boxes)[1]

    # Create a tensor for batch indices, shape: [batch_size, num_boxes, 1]
    box_ind = tf.tile(tf.range(batch_size)[:, tf.newaxis], [1, num_boxes])
    
    # Draw the bounding boxes on the images.
    images_with_boxes = tf.image.draw_bounding_boxes(images, boxes, colors)

    return images_with_boxes

# Example usage:
# Sample images tensor [1, 100, 100, 3] (1 image of 100x100 with 3 color channels)
images = tf.random.uniform(shape=[1, 100, 100, 3], minval=0, maxval=1)

# Sample boxes tensor [1, 1, 4] (1 box per image)
boxes = tf.constant([[[0.1, 0.1, 0.6, 0.6]]], dtype=tf.float32)

# Sample colors tensor [1, 1, 3] (1 color per box)
colors = tf.constant([[[1.0, 0.0, 0.0]]])

# Draw the bounding boxes
output_images = draw_bounding_boxes(images, boxes, colors)

# Verify the output
print(output_images)
