import tensorflow as tf

def resize_images(images, new_shape):
    images_resized = tf.image.resize(images, new_shape)
    return images_resized

# Let's test the function
# input images, it should be a tensor of shape (batch_size, height, width, channels)
images = tf.random.normal([32, 32, 32, 3])
new_shape = (64, 64)

# Call the function
resized_images = resize_images(images, new_shape)

# The shape should be (batch_size, new_height, new_width, channels)
print(resized_images.shape)
