import tensorflow as tf

def crop_and_resize_tensor_image(image_tensor, crop_size):
    # The function to be implemented
    pass

def resize_images(images, new_size):
    # Resizes a list of images to a new size
    # images: a tensor containing a batch of images
    # new_size: a list or tuple, [new_height, new_width]

    return tf.image.resize(images, new_size)

# Testing the functions
image_tensor = tf.random.uniform([300, 300, 3])  # Assuming a batch size of 1
new_size = [200, 200]  # New size for cropped and resized images

# Extracting crops
crops = crop_and_resize_tensor_image(image_tensor, 100)

# Resizing crops
resized_images = resize_images(crops, new_size)
