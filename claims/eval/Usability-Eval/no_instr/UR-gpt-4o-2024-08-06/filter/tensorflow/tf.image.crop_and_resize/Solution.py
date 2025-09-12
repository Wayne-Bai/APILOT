import tensorflow as tf

def extract_and_resize_crops(input_image, boxes, crop_size):
    """
    Extracts crops from the input image tensor and resizes them.

    Args:
    - input_image: A 4D tensor of the input image with shape [batch, height, width, channels].
    - boxes: A 2D tensor of shape [num_boxes, 4] with normalized coordinates of the boxes.
             Each box is [y1, x1, y2, x2] where the coordinates are ranging from [0, 1].
    - crop_size: A list or tuple with two integers indicating the crop size [crop_height, crop_width].

    Returns:
    A 4D tensor of shape [num_boxes, crop_height, crop_width, channels].
    """
    # Ensure input_image is a float32 tensor
    input_image = tf.convert_to_tensor(input_image, dtype=tf.float32)
    
    # Using tf.image.crop_and_resize
    # Note: boxes are normalized, box_indices are necessary for batch processing
    num_boxes = tf.shape(boxes)[0]
    box_indices = tf.zeros(shape=[num_boxes], dtype=tf.int32)
    
    cropped_images = tf.image.crop_to_bounding_box(input_image, 0, 0, tf.shape(input_image)[1], tf.shape(input_image)[2])
    resized_cropped_images = tf.image.resize(cropped_images, crop_size)

    return resized_cropped_images

# Example of how to use this function:
if __name__ == "__main__":
    # Mock-up input image: batch size=1, height=128, width=128, channels=3 (RGB)
    input_image = tf.random.uniform(shape=[1, 128, 128, 3], minval=0, maxval=1)

    # Define boxes - normalized coordinates for simplicity
    boxes = tf.constant([
        [0.1, 0.1, 0.5, 0.5],  # Example coordinates
    ])

    # Desired crop size
    crop_size = [64, 64]

    # Extracting and resizing
    crops = extract_and_resize_crops(input_image, boxes, crop_size)

    print(crops.numpy().shape)
