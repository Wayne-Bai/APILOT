import tensorflow as tf

def draw_bounding_boxes_on_images(images, boxes):
    """
    Draws bounding boxes on a batch of images.

    Parameters:
    images (tf.Tensor): A 4-D tensor of shape [batch_size, height, width, channels].
    boxes (tf.Tensor): A 2-D tensor of shape [num_boxes, 4] with each box defined by 
                       [y_min, x_min, y_max, x_max] in normalized coordinates.

    Returns:
    tf.Tensor: A tensor representing the images with bounding boxes drawn on them.
    """
    # Ensure the images are of rank 4
    assert images.shape.ndims == 4, "Images tensor must be of shape [batch_size, height, width, channels]"
    
    # Draw bounding boxes
    return tf.image.draw_bounding_boxes(images, tf.expand_dims(boxes, axis=0))

# Example usage
batch_images = tf.random.uniform(shape=[2, 256, 256, 3])  # Example batch of images
bounding_boxes = tf.constant([[0.1, 0.1, 0.9, 0.9], [0.2, 0.2, 0.5, 0.5]])  # Example bounding boxes

result_images = draw_bounding_boxes_on_images(batch_images, bounding_boxes)

# To visualize the drawn images, you can convert them to numpy or use a plotting library 
