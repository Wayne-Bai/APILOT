
import tensorflow as tf

def resize_image(image, new_height, new_width, method='bilinear'):
    if method == 'nearest':
        return tf.image.resize(image, [new_height, new_width], method=tf.image.ResizeMethod.NEAREST_NEIGHBOR)
    elif method == 'bicubic':
        return tf.image.resize(image, [new_height, new_width], method=tf.image.ResizeMethod.BICUBIC)
    else:
        return tf.image.resize(image, [new_height, new_width], method=tf.image.ResizeMethod.BILINEAR)
