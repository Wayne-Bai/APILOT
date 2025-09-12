import tensorflow as tf

def draw_bounding_boxes(images, bounding_boxes, colors):
    """
    Draw bounding boxes on a batch of images.

    Args:
        images: tf.Tensor, a batch of image tensors.
        bounding_boxes: tf.Tensor, a tensor of shape (batch_size, num_boxes, 2)
                         containing bounding box coordinates (x_min, y_min, x_max, y_max) normalized to [0, 1].
        colors: List[tuple], list of colors for the bounding boxes, in the format [r, g, b] or [a, r, g, b] for RGBA.

    Returns:
        tf.Tensor, an updated batch of image tensors with bounding boxes drawn on them.
    """
    def draw_box(image, box, color):
        """
        Draw a bounding box on a single image.

        Args:
            image: tf.Tensor, an image tensor to draw on.
            box: tf.Tensor, a tensor of shape (4,) containing bounding box coordinates (x_min, y_min, x_max, y_max) normalized to [0, 1].
            color: tuple, a color for the bounding box.

        Returns:
            tf.Tensor, the image tensor with a bounding box drawn on it.
        """
        # Convert normalized coordinates
        x_min, y_min, x_max, y_max = map(int, box * tf.constant([tf.shape(image)[1], tf.shape(image)[0], tf.shape(image)[1], tf.shape(image)[0]]))
        image_with_box = image[:, y_min:y_max, x_min:x_max, :]
        image_with_box = tf.image.draw_bounding_boxes(image_with_box, [[tf.constant([x_min, y_min, x_max, y_max])]])
        return tf.image.combine_images(image_with_box, image[:, :y_min, :, :])[0]

    draw_bounding_boxes_single_image_op = tf.raw_ops.DrawBoundingBoxes(v=images, bounding_boxes=bounding_boxes, colors=colors)
    return draw_bounding_boxes_single_image_op

# Example usage:
# images = tf.random.normal([batch_size, height, width, channels])
# bounding_boxes = tf.random.uniform([batch_size, num_boxes, 4], minval=0, maxval=1)
# colors = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]  # Define colors for the bounding boxes
# output = draw_bounding_boxes(images, bounding_boxes, colors)
