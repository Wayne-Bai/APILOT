
import tensorflow as tf

def crop_and_resize_images(images, boxes, box_index, crop_size):
    cropped_images = tf.image.crop_and_resize(images, boxes, box_index, crop_size)
    return cropped_images
