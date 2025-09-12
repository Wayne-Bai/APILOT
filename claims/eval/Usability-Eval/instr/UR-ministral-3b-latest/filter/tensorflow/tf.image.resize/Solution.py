import tensorflow as tf
# Define the image size
image_size = (128, 128)

def resize_image(image, size):
    image = tf.image.resize(image, size)
    return image

# Example usage
image = tf.placeholder(tf.uint8, shape=(None, None, 3))
resized_image = resize_image(image, image_size)
