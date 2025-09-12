
import tensorflow as tf

def draw_bounding_boxes(images, boxes, colors):
    boxed_images = tf.image.draw_bounding_boxes(images, boxes)
    return boxed_images
