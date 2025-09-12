# Import necessary libraries
import tensorflow as tf

def extract_and_resize_crops(image, boxes, box_indices, crop_size):
    """
    Extracts crops from the input image tensor and resizes them.

    Args:
    - image: Input image tensor.
    - boxes: Normalized coordinates of the bounding boxes.
    - box_indices: The index of the image to which each box belongs.
    - crop_size: The size of the crops to extract.

    Returns:
    - crops: A tensor of extracted and resized crops.
    """
    # Use tf.image.crop_and_resize to extract and resize crops
    crops = tf.image.crop_and_resize(
        image, boxes, box_indices, crop_size=crop_size,
        method='bilinear', extrapolation_value=0.0,
        name='crop_and_resize'
    )
    return crops

# Example usage:
# Assuming the image is of shape (height, width, channels)
image = tf.random.uniform(shape=(256, 256, 3))

# Define the bounding box coordinates and indices
boxes = tf.constant([[0.1, 0.1, 0.9, 0.9]])
box_indices = tf.constant([0])
box_indices = tf.expand_dims(box_indices, axis=1)

# Define the crop size
crop_size = (224, 224)

# Extract and resize crops
crops = extract_and_resize_crops(image, boxes, box_indices, crop_size)
print(crops.shape)
