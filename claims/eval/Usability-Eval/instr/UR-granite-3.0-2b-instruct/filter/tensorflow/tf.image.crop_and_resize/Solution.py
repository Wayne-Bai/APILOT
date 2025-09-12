import tensorflow as tf

# Define the input image tensor
input_image = tf.random.normal([10, 10, 3])

# Define the crop size
crop_size = 5

# Extract the crops from the input image tensor
crops = tf.extract_image_patches(input_image, sizes=[1, crop_size, crop_size, 1], strides=[1, 1, 1, 1], padding='VALID')

# Resize the crops to a specified size
resized_crops = tf.image.resize(crops, [10, 10])

# Print the shape of the resized crops
print(resized_crops.shape)
