import tensorflow as tf

def draw_bounding_boxes(images, boxes):
    bboxes = box_interpreter(boxes)
    bboxes = tf.cast(bboxes, tf.int32)
    heights = tf.cast(images.shape[1], tf.int32)
    widths = tf.cast(images.shape[2], tf.int32)

    def box_interpreter(boxes):
        bboxes = boxes
        bboxes[:, 2] = bboxes[:, 2] * 1.0 * heights
        bboxes[:, 3] = bboxes[:, 3] * 1.0 * widths
        return bboxes

    def draw_box(image, box):
        return tf.image.draw_bounding_box(
            image,
            box[1],
            box[2],
            box[3],
            box[4],
            alpha=0.5,
        )

    images = tf.map_fn(lambda x: tf.map_fn(lambda y: draw_box(x, y), bboxes), tf.boolean_mask(images, bboxes))

    return images

# Example usage
images = tf.random.uniform((100, 256, 256, 3))  # Batch of 100 images, for example
boxes = tf.constant([[0.5, 0.5, 0.3, 0.3], [0.7, 0.7, 0.8, 0.8]])  # Boxes with normalized coordinates [x_min, y_min, x_max, y_max]
bounding_box_images = draw_bounding_boxes(images, boxes)
