import tensorflow as tf

def draw_boxes_on_images(images, boxes):
    batched_images = tf.image.draw_bounding_boxes(
        images=images,
        boxes=boxes)

    return batched_images
