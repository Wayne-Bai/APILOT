import tensorflow as tf
def extract_and_resize_crops(image_tensor, crop_size, num_crops):
    # Extract crops from the image tensor
    crops = tf.image.extract_glimpse(image_tensor, [crop_size, crop_size], num_crops=num_crops)
    # Resize the crops to a fixed size
    resized_crops = tf.image.resize_images(crops, [224, 224])
    return resized_crops
