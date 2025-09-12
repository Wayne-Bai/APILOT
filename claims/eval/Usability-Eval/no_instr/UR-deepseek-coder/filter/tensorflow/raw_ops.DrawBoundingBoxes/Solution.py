import tensorflow as tf

def draw_bounding_boxes(images, boxes):
    # Ensure images and boxes are tensors
    images = tf.convert_to_tensor(images, dtype=tf.float32)
    boxes = tf.convert_to_tensor(boxes, dtype=tf.float32)

    # Ensure the images are in the correct format (NHWC)
    if len(images.shape) != 4:
        raise ValueError("Images must be a batch of images with shape (batch_size, height, width, channels).")

    # Ensure the boxes are in the correct format (Nx4)
    if len(boxes.shape) != 3 or boxes.shape[2] != 4:
        raise ValueError("Boxes must be a batch of bounding boxes with shape (batch_size, num_boxes, 4).")

    # Draw bounding boxes on the images
    image_with_boxes = tf.image.draw_bounding_boxes(images, boxes)

    return image_with_boxes

# Example usage:
# images: a batch of images with shape (batch_size, height, width, channels)
# boxes: a batch of bounding boxes with shape (batch_size, num_boxes, 4)
# images = ...
# boxes = ...
# result = draw_bounding_boxes(images, boxes)
