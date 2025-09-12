import tensorflow as tf

def extract_and_resize_crops(image_tensor):
    # Extract crops from the input image tensor
    crops = tf.image.extract_patches(image_tensor, sizes=[1, 7, 7, 1], strides=[1, 4, 4, 1], rates=[1, 1, 1, 1], padding='SAME')
    
    # Resize the crops to a fixed size
    resized_crops = tf.image.resize(crops, [28, 28])
    
    return resized_crops
