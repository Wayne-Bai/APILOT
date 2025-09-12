
import tensorflow as tf

def draw_bounding_boxes(images, boxes):
    """Draw bounding boxes on a batch of images.

    Args:
        images (tf.Tensor): The input images. Shape: [batch_size, height, width, channels].
        boxes (tf.Tensor): The bounding box coordinates. Shape: [batch_size, num_boxes, 4]. Each element in the tensor represents a single bounding box, with the format [xmin, ymin, xmax, ymax].

    Returns:
        tf.Tensor: The drawn images. Shape: [batch_size, height, width, channels].
    """
    # Check input shapes
    if len(images.shape) != 4 or len(boxes.shape) != 3:
        raise ValueError("Invalid input shape. Expected images and boxes to be four-dimensional tensors.")

    # Get the image dimensions
    height, width = images.shape[1], images.shape[2]

    # Generate a canvas with zeroes
    canvas = tf.zeros_like(images)

    # Iterate over each image in the batch
    for i in range(boxes.shape[0]):
        # Iterate over each bounding box for this image
        for j in range(boxes.shape[1]):
            # Get the coordinates of this bounding box
            xmin, ymin, xmax, ymax = boxes[i, j, :]

            # Draw a rectangle on the canvas
            canvas[i, ymin:ymax, xmin:xmax] = 1

    return canvas
