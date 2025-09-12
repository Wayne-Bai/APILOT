import tensorflow as tf

# Load the input image tensor
input_image = tf.placeholder(shape=(1, 256, 256, 3), dtype=tf.float32)

# Define the size of the crops
crop_size = (64, 64)

# Define the offsets of the crops
offsets = ((0, 0), (64, 0), (128, 0))

# Extract and resize the crops using tf.image.extract_glimpse
crops = [tf.image.extract_glimpse(input_image, crop_size=crop_size[i], offset=offsets[i]) for i in range(3)]

# Resize the extracted crops to the desired size using tf.image.resize_images
resized_crops = [tf.image.resize_images(crops[i], size=(256, 256)) for i in range(3)]
