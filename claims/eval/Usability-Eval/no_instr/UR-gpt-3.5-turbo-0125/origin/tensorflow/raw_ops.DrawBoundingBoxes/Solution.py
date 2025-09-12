
import tensorflow as tf

def draw_bounding_boxes(images, boxes, colors, name=None):
    return tf.raw_ops.DrawBoundingBoxes(images=images, boxes=boxes, colors=colors, name=name)
