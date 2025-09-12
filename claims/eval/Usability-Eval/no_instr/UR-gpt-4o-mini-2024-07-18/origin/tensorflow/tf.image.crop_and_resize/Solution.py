import tensorflow as tf

def extract_and_resize_crops(image_tensor, crop_sizes, offsets):
    """
    Extract crops from the input image tensor and resize them.

    Parameters:
    - image_tensor: A 4-D Tensor of shape [batch_size, height, width, channels].
    - crop_sizes: A tensor of shape [N, 2] containing the height and width of the crops.
    - offsets: A tensor of shape [N, 2] containing the y and x offsets from which to extract crops.

    Returns:
    - resized_crops: A 4-D Tensor of shape [N, new_height, new_width, channels] after resizing.
    """
    batch_size, img_height, img_width, channels = image_tensor.shape

    resized_crops = []
    for i in range(len(crop_sizes)):
        crop_height, crop_width = crop_sizes[i]
        offset_y, offset_x = offsets[i]
        
        # Extract the crop
        crop = tf.image.crop_to_bounding_box(image_tensor, offset_y, offset_x, crop_height, crop_width)
        
        # Resize the crop (example size, adjust as needed)
        new_height, new_width = 100, 100  # Example resizing dimensions
        crop_resized = tf.image.resize(crop, [new_height, new_width])
        
        resized_crops.append(crop_resized)

    return tf.stack(resized_crops)
