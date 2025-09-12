import tensorflow as tf

@tf.function
def draw_bounding_boxes(image, bboxes, colors):
    shape = tf.shape(image)
    image_height = shape[1]
    image_width = shape[2]

    for i in range(tf.shape(bboxes)[0]):
        bbox = bboxes[i]
        x1, y1, x2, y2 = bbox
        x1 = tf.cast(x1, dtype=tf.int64)
        y1 = tf.cast(y1, dtype=tf.int64)
        x2 = tf.cast(x2, dtype=tf.int64)
        y2 = tf.cast(y2, dtype=tf.int64)

        x3 = image_width - x2
        y3 = image_height - y2

        x1, y1, x2, y2 = tf.cast([x1, y1, image_width - x3, image_height - y3], dtype=tf.int64)
        color = colors[i]

        image = tf.image.crop_to_bounding_box(
            image, y1, x1, y2 - y1, x2 - x1)
        image = tf.image.circle(image, shape=(tf.shape(image)[1], tf.shape(image)[2], 3), center=(y2 // 2 + y1 // 2, x2 // 2 + x1 // 2), radius=10)

        image = tf.image.crop_to_bounding_box(image, y2 - y1, x2 - x1, 1, 1, output_height=shape[1], output_width=shape[2], fill_value=color)
    return image

# Example usage:
image = tf.random.uniform((100, 150, 150, 3))
bboxes = [[50, 50, 100, 100], [150, 50, 200, 100]]
colors = [tf.range(3), tf.range(3)]

output_image = draw_bounding_boxes(image, bboxes, colors)
