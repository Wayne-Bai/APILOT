import tensorflow as tf

def crop_and_resize(image, boxes, target_size):
    # Crop the image tensor using the provided boxes
    crops = tf.image.crop_and_resize(image, boxes, box_indices=tf.range(tf.shape(boxes)[0]), target_size=target_size)

    # Resize the crops to the target size using bilinear interpolation
    resized_crops = tf.image.resize(crops, target_size, method=tf.image.ResizeMethod.BILINEAR)

    return resized_crops
