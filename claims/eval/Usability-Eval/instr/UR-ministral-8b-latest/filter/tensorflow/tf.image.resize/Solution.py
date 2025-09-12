import tensorflow as tf

def resize_image(image, target_size):
    """Resize the image to the target size."""
    image = tf.cast(image, tf.float32)
    image = tf.image.resize(image, target_size)
    return image

# Example usage:
# Assuming you have an image Tensor
image = tf.random.normal([256, 256, 3])

# Define the target size
target_size = [128, 128]

# Resize the image
resized_image = resize_image(image, target_size)

print(resized_image.shape)  # Should output (128, 128, 3)
