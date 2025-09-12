import tensorflow as tf

def extract_and_resize_crops(image_tensor, boxes, crop_size):
    """
    Extracts crops from the input image tensor and resizes them.
    
    Parameters:
    - image_tensor: A 4-D tensor of shape [batch_size, height, width, channels].
    - boxes: A tensor of shape [num_boxes, 4] where each row represents
             a bounding box in normalized coordinates [y_min, x_min, y_max, x_max].
    - crop_size: A tuple (new_height, new_width) specifying the size to resize cropped images.
    
    Returns:
    - A tensor of resized crops with shape [num_boxes, new_height, new_width, channels].
    """
    crops = tf.image.crop_and_resize(image_tensor, boxes, tf.zeros((tf.shape(boxes)[0],), dtype=tf.int32), crop_size)
    return crops

# Example usage
# image_tensor_shape = [1, 256, 256, 3]
# image_tensor = tf.random.uniform(shape=image_tensor_shape)
# boxes = tf.convert_to_tensor([[0.1, 0.1, 0.5, 0.5], [0.2, 0.2, 0.6, 0.6]], dtype=tf.float32)
# crop_size = (128, 128)

# resized_crops = extract_and_resize_crops(image_tensor, boxes, crop_size)
