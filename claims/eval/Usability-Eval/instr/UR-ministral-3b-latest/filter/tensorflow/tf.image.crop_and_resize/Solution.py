import tensorflow as tf

# Define a function to crop the image
def crop_and_resize(image_tensor, crop_size=(224, 224)):
    # Get the height and width of the image
    h, w = image_tensor.shape[:2]

    # Calculate the padding needed to crop to the desired size
    pad_w = crop_size[1] - w
    pad_h = crop_size[0] - h

    # Crop the image along the y-axis (vertical) and x-axis (horizontal)
    tl, tr, bl, br = tf.image.pad(image_tensor)  # pad the image with constants
    cropped_tensor = image_tensor[tf.maximum(tf.floor(tl), tf.zeros_like(tl)):tf.minimum(tl + crop_size[0], tf.zeros_like(tl) + crop_size[0]),
                                 tf.maximum(tf.floor(tr), tf.zeros_like(tr)):tf.minimum(tr + crop_size[1], tf.zeros_like(tr) + crop_size[1])]

    return cropped_tensor

# Example tensor
image_tensor = tf.random.normal([256, 256, 3])  # Random image tensor of 256x256 with 3 channels

# Crop and resize the image tensor
cropped_image = crop_and_resize(image_tensor)
print(cropped_image.shape)
