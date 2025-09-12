import tensorflow as tf

def crop_and_resize(image, boxes, sizes):
    """
    Extracts crops from the input image tensor and resizes them.

    :param image: A 4-D tensor of shape [batch, height, width, channels].
    :param boxes: A 2-D tensor of shape [num_boxes, 4] containing the coordinates
                  of the boxes to crop in the format [y_min, x_min, y_max, x_max].
    :param sizes: A 2-D tensor of shape [num_boxes, 2] containing the target sizes
                  in the format [target_height, target_width] for each box.
    :return: A 4-D tensor of cropped and resized images.
    """
    # Use tf.image.crop_and_resize to extract and resize the crops
    return tf.image.crop_and_resize(image, boxes, tf.zeros(tf.shape(boxes)[0], dtype=tf.int32), sizes)

# Example usage
if __name__ == "__main__":
    # Create a sample image tensor (batch_size=1, height=100, width=100, channels=3)
    image = tf.random.uniform(shape=[1, 100, 100, 3])

    # Define the boxes (y_min, x_min, y_max, x_max)
    boxes = tf.constant([[0.1, 0.1, 0.7, 0.7]])  # Example box

    # Define the target sizes for the crops
    sizes = tf.constant([[50, 50]])  # Resize to 50x50

    # Extract and resize crops
    crops = crop_and_resize(image, boxes, sizes)

    print(crops.shape)  # Output shape should be [num_boxes, target_height, target_width, channels]
