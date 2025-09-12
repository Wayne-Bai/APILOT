import tensorflow as tf

def extract_resize_crops(input_image):
    # Define the crop size and step size
    crop_size = [224, 224]
    step_size = [16, 16]

    # Extract crops from the input image using tf.image.extract_glimpse
    crops = tf.image.extract_glimpse(input_image, size=crop_size, offsets=[0, 0], centered=True, noise='uniform')

    # Resize the crops to the desired size using tf.image.resize
    resized_crops = tf.image.resize(crops, size=[224, 224])

    return resized_crops
