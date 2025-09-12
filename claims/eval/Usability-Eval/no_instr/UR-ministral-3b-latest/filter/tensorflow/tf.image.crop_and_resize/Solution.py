import tensorflow as tf

def crop_and_resize(image_tensor, box, size):
    # Extract crops from the input image tensor
    y1, x1, y2, x2 = box
    y1, y2, x1, x2 = tf.cast(y1, tf.int32), tf.cast(y2, tf.int32), tf.cast(x1, tf.int32), tf.cast(x2, tf.int32)

    # Get the crop from the image tensor
    crop = tf.image.crop_to_bounding_box(image_tensor, y1, x1, y2, x2)

    # Resize the crop
    resized_crop = tf.image.resize(crop, size)

    return resized_crop
