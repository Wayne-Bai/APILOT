import tensorflow as tf

def extract_and_resize(input_image, boxes, box_indices, crop_size):
    """
    Extracts crops from the input image tensor and resizes them.

    :param input_image: A 4-D tensor of shape [batch, height, width, channels].
    :param boxes: A 2-D tensor of shape [num_boxes, 4]. Each row is in the format [y1, x1, y2, x2].
    :param box_indices: A 1-D tensor of shape [num_boxes] with int32 values in [0, batch).
    :param crop_size: A tuple specifying the output size of the crops as [crop_height, crop_width].
    :return: A 4-D tensor of shape [num_boxes, crop_height, crop_width, channels].
    """
    # Convert boxes to a normalized format required by crop_and_resize
    num_boxes = tf.shape(boxes)[0]
    box_indices = tf.cast(box_indices, tf.int32)
    
    # Extract crops
    crops = tf.image.crop_and_resize(input_image, boxes, box_indices, crop_size)
    
    return crops

# Example usage
# Let's assume we have a batch of 2 images
batch_size = 2
height = 300
width = 300
channels = 3
input_image = tf.random.uniform((batch_size, height, width, channels), dtype=tf.float32)

# Define boxes as [y1, x1, y2, x2]
boxes = tf.constant([[0.1, 0.1, 0.5, 0.5], [0.2, 0.2, 0.7, 0.7]], dtype=tf.float32)

# Indices of the respective box from each image in the batch
box_indices = tf.constant([0, 1], dtype=tf.int32)

# Define the desired size for resized crops
crop_size = (100, 100)

# Extract and resize crops
crops = extract_and_resize(input_image, boxes, box_indices, crop_size)

# Run in a TensorFlow session in eager execution (default in TF 2.x)
print(crops.shape)
