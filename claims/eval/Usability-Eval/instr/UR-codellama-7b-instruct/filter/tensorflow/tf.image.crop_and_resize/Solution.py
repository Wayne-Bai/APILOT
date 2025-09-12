
import tensorflow as tf

def crop_and_resize(image, size):
    # Crop the input image into non-overlapping patches
    patches = tf.extract_patches(tf.shape(image), 10, strides=1)
    
    # Resize each patch to the desired size
    resized_patches = tf.image.resize(patches, size)
    
    return resized_patches
