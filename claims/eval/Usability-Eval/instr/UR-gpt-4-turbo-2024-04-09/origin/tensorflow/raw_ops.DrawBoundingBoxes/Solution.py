import tensorflow as tf

def draw_bounding_boxes(images, boxes):
    """
    Draw bounding boxes on a batch of images.
    
    Args:
    images : 4-D Tensor of shape `[batch, height, width, channels]`.
    boxes  : 3-D Tensor of shape `[batch, num_boxes, 4]` containing the normalized
             coordinates of the boxes to draw where each box is [y_min, x_min, y_max, x_max].

    Returns:
    Tensor of the same type and shape as `images`, with bounding boxes drawn.
    """
    return tf.image.draw_bounding_boxes(images, boxes)

# Example usage:
# Create a batch of 2 images of size 200x200 with 3 color channels (RGB).
batch_size = 2
height, width = 200, 200
num_channels = 3

# Random image batch for demonstration
images = tf.random.uniform(shape=(batch_size, height, width, num_channels))

# Define bounding boxes for each image.
# Each box is specified by (y_min, x_min, y_max, x_max) with values normalized between [0, 1]
boxes = tf.constant([[[0.1, 0.2, 0.5, 0.8], [0.3, 0.1, 0.4, 0.4]],  # Boxes for image 1
                     [[0.2, 0.3, 0.8, 0.9]]], dtype=tf.float32)    # Boxes for image 2

# Draw bounding boxes on images
images_with_boxes = draw_bounding_boxes(images, boxes)
