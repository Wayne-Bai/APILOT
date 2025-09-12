import tensorflow as tf

# Assuming 'input_image' is your input image tensor
input_image = tf.placeholder(tf.float32, shape=(None, None, 3))

# Cropping the input image
cropped_image = tf.slice(input_image, begin=[0, 0, 0], size=[HEIGHT, WIDTH, 3])

# Resizing the cropped image
resized_image = tf.image.resize(cropped_image, [RESIZE_HEIGHT, RESIZE_WIDTH])

# Print the resized image
print(resized_image)
