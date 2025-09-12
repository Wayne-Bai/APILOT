import tensorflow as tf

def draw_bounding_boxes(images, boxes, colors):
    # Ensure the images tensor is in the correct format
    images = tf.convert_to_tensor(images, dtype=tf.float32)
    boxes = tf.convert_to_tensor(boxes, dtype=tf.float32)
    colors = tf.convert_to_tensor(colors, dtype=tf.float32)

    # Expand dimensions of the colors tensor to match the number of boxes
    colors = tf.expand_dims(colors, axis=0)

    # Draw bounding boxes on the images
    image_with_boxes = tf.image.draw_bounding_boxes(images, boxes, colors)

    return image_with_boxes

# Example usage:
# images: a batch of images with shape [batch_size, height, width, channels]
# boxes: bounding boxes with shape [batch_size, num_boxes, 4] where each box is [y_min, x_min, y_max, x_max]
# colors: colors for the bounding boxes with shape [num_boxes, 3] (RGB values)

# Example data
images = tf.random.uniform((2, 224, 224, 3), minval=0, maxval=255, dtype=tf.float32)
boxes = tf.constant([[[0.1, 0.2, 0.5, 0.6], [0.3, 0.4, 0.7, 0.8]], [[0.2, 0.3, 0.6, 0.7], [0.4, 0.5, 0.8, 0.9]]])
colors = tf.constant([[255, 0, 0], [0, 255, 0]])

# Draw bounding boxes on the images
result = draw_bounding_boxes(images, boxes, colors)

# Display the result (if running in a compatible environment)
# tf.print(result)
