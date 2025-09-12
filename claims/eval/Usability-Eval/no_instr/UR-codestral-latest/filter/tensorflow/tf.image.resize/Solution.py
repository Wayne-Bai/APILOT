import tensorflow as tf

def resize_images(image_list, size, method):
    resized_images = []
    for image in image_list:
        resized_image = tf.image.resize(image, size, method=method)
        resized_images.append(resized_image)
    return resized_images
