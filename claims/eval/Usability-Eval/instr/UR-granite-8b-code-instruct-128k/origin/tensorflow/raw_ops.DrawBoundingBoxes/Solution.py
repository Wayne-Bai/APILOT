import tensorflow as tf

def draw_bounding_boxes(images, boxes):
    return tf.raw_ops.DrawBoundingBoxes(images=images, boxes=boxes)
