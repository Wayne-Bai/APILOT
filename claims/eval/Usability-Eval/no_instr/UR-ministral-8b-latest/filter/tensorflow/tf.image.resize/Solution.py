import tensorflow as tf

def resize_image(image, target_shape):
    image = tf.image.resize(image, target_shape)
    return image

# Example usage
image = tf.random.uniform((256, 256, 3))  # Example image tensor
target_shape = (128, 128)  # Target shape to resize to
resized_image = resize_image(image, target_shape)
