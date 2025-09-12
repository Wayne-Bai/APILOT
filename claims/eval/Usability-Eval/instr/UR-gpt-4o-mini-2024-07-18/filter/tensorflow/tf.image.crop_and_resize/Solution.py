import tensorflow as tf

def crop_and_resize_images(input_image, boxes, size):
    """
    Crops and resizes the images from the input tensor.
    
    Parameters:
    - input_image: A 4D tensor of shape [batch, height, width, channels].
    - boxes: A 2D tensor of shape [num_boxes, 4] containing bounding box coordinates
             in the format [y1, x1, y2, x2], where y1 and y2 are the vertical coordinates and
             x1 and x2 are the horizontal coordinates, normalized to [0, 1].
    - size: A 1D tensor of shape [2] containing [new_height, new_width].
    
    Returns:
    - A tensor of cropped and resized images.
    """
    
    cropped_images = tf.image.crop_and_resize(input_image, boxes, tf.range(tf.shape(boxes)[0]), size)
    return cropped_images

# Example usage
input_image = tf.random.uniform([1, 256, 256, 3])  # Example input image tensor
boxes = tf.constant([[0.1, 0.1, 0.5, 0.5], [0.3, 0.3, 0.7, 0.7]])  # Example bounding boxes
size = tf.constant([64, 64])  # Resize to 64x64

cropped_resized_images = crop_and_resize_images(input_image, boxes, size)
