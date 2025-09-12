import tensorflow as tf

def draw_bounding_boxes(images, boxes, colors):
    """
    Draws bounding boxes on a batch of images.
    
    Args:
    images: A 4-D tensor of shape [batch, height, width, channels].
    boxes: A 3-D tensor of shape [batch, num_boxes, 4], where each box is represented
           by [y_min, x_min, y_max, x_max] in normalized coordinates.
    colors: A 2-D tensor of shape [num_boxes, 3] to specify the colors of the boxes.
    
    Returns:
    A 4-D tensor with bounding boxes drawn on the original images.
    """
    
    # Ensure that boxes are in the shape [batch, num_boxes, 4]
    boxes = tf.convert_to_tensor(boxes)

    # Draw the bounding boxes on the images
    images_with_boxes = tf.image.draw_bounding_boxes(images, boxes, colors)
    
    return images_with_boxes

# Example usage
if __name__ == "__main__":
    # Create dummy images
    batch_size = 2
    height = 100
    width = 100
    channels = 3
    images = tf.random.uniform((batch_size, height, width, channels))

    # Define bounding boxes [y_min, x_min, y_max, x_max] in normalized coordinates
    boxes = [[[0.1, 0.1, 0.5, 0.5], [0.3, 0.3, 0.7, 0.7]],
             [[0.2, 0.2, 0.8, 0.8]]]

    # Define colors for the boxes
    colors = tf.constant([[1, 0, 0], [0, 1, 0]], dtype=tf.float32)  # Red and Green

    # Draw bounding boxes
    output_images = draw_bounding_boxes(images, boxes, colors)

    # To visualize the output, you can convert the tensor to numpy and use a library like matplotlib
    import matplotlib.pyplot as plt

    for i in range(batch_size):
        plt.imshow(output_images[i].numpy())
        plt.axis('off')
        plt.show()
