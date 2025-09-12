import tensorflow as tf

def resize_image(image, size):
    image = tf.image.resize(image, size)
    return image

# Load an image
image = tf.image.decode_jpeg(tf.io.read_file('image.jpg'), channels=3)

# Resize the image
resized_image = resize_image(image, (224, 224))

# Print the shape of the resized image
print(resized_image.shape)
