import tensorflow as tf

def draw_bounding_boxes(images, boxes, colors):
    """Draws bounding boxes on a batch of images.

    Args:
    images: A uint8 tensor of shape [batch_size, height, width, 3]
    boxes: A float32 tensor of shape [batch_size, num_boxes, 4] containing the bounding box coordinates
    colors: A float32 tensor of shape [batch_size, num_boxes, 3] containing the RGB values for each bounding box

    Returns:
    A uint8 tensor of shape [batch_size, height, width, 3] with bounding boxes drawn on the images
    """
    batch_size, height, width, _ = images.get_shape().as_list()
    num_boxes = boxes.get_shape().as_list()[1]

    for i in range(batch_size):
        for j in range(num_boxes):
            x1, y1, x2, y2 = boxes[i, j]
            color = colors[i, j]
            image = images[i]
            image = tf.reshape(image, [height, width, 3])
            image = tf.cast(image, tf.float32)
            image = tf.image.draw_bounding_boxes(image, tf.expand_dims(boxes[i], axis=0), colors=tf.expand_dims(colors[i], axis=0))
            image = tf.cast(image, tf.uint8)
            images[i] = image

    return images
