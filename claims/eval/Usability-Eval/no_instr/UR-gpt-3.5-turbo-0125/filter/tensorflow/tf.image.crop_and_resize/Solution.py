
import tensorflow as tf

def crop_and_resize_images(images, boxes, box_indices, crop_size):
    """
    Extracts crops from the input image tensor and resizes them.
    
    Args:
        images: A 4-D float Tensor of shape [batch, image_height, image_width, depth].
        boxes: A 2-D Tensor of type float. The bounding box coordinates in the following format:
               [y1, x1, y2, x2].
        box_indices: A 1-D Tensor of type int32, the component to choose along the batch dimension.
        crop_size: A 1-D Tensor of 2 elements: size of the crop [crop_height, crop_width].
        
    Returns:
        A 4-D float Tensor of shape [num_boxes, crop_height, crop_width, depth].
    """
    cropped_images = tf.image.crop_and_resize(images, boxes, box_indices, crop_size)
    return cropped_images
