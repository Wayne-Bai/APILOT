import tensorflow as tf

def draw_bounding_boxes(images, bounding_boxes):
    # Convert bounding boxes to tensor
    bounding_boxes = tf.convert_to_tensor(bounding_boxes)

    # Create a zeros tensor of the same shape as the input images
    images_with_boxes = tf.zeros_like(images)

    # Overlay the bounded boxes on the images
    images_with_boxes = tf.raw_ops.DrawBoundingBoxes(
        images=images,
        boxes=bounding_boxes,
        colors=[255.0, 0.0, 0.0, 1.0],  # RGBA values for red color
        thickness=2,
        clip=True)

    return images_with_boxes
