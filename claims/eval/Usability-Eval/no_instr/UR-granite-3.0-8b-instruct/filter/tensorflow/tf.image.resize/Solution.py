import tensorflow as tf

def resize_images(images, size, method):
    # Ensure the method is valid
    if method not in ['nearest', 'bilinear', 'bicubic', 'area', 'bicubic_auto']:
        raise ValueError("Invalid resizing method. Choose from 'nearest', 'bilinear', 'bicubic', 'area', 'bicubic_auto'.")

    # Resize the images using the specified method
    resized_images = tf.image.resize(images, size, method=method)

    return resized_images
