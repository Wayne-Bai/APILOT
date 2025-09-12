import tensorflow as tf

def draw_bounding_boxes(images, boxes):
    """
    Draws bounding boxes on a batch of images.
    
    Args:
    images (tf.Tensor): A 4-D float tensor of shape [batch, height, width, channels].
                         Normalized image values should lie between 0 and 1.
    boxes (tf.Tensor): A 3-D float tensor of shape [batch, num_boxes, 4] containing the 
                       bounding box coordinates [y_min, x_min, y_max, x_max], normalized
                       between 0 and 1.

    Returns:
    tf.Tensor: A 4-D float tensor of the same shape as 'images' with bounding boxes
               drawn on the images.
    """
    # Draw bounding boxes using the raw_ops draw method
    images_with_boxes = tf.image.draw_bounding_boxes(images, boxes)
    
    return images_with_boxes

# Example usage
if __name__ == "__main__":
    # Create sample batch of images and bounding boxes
    batch_size = 2
    height, width, channels = 256, 256, 3
    num_boxes = 1

    # Create dummy images
    images = tf.random.uniform(shape=[batch_size, height, width, channels], minval=0, maxval=1)
    
    # Create example bounding boxes. Normalized [y_min, x_min, y_max, x_max]
    boxes = tf.constant([[[0.1, 0.2, 0.5, 0.8]], [[0.3, 0.1, 0.4, 0.5]]], dtype=tf.float32)
    
    # Draw bounding boxes on images
    images_with_boxes = draw_bounding_boxes(images, boxes)
    
    # Display the images using matplotlib (optional)
    import matplotlib.pyplot as plt

    for img in images_with_boxes:
        plt.figure()
        plt.imshow(img)
        plt.show()
