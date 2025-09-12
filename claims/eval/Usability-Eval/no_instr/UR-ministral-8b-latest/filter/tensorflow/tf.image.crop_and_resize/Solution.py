import tensorflow as tf

def crop_and_resize(image_tensor, target_size):
    # Extract crops from the input image tensor using a specific method (e.g., random crops)
    cropped_tensors = tf.image.random_crop(image_tensor, target_size)

    # Resize the cropped image tensor
    resized_tensors = tf.image.resize(cropped_tensors, target_size)

    return resized_tensors
