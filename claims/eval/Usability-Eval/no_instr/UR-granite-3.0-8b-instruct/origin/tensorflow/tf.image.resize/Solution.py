import tensorflow as tf

def resize_images(images, size, method):
    return tf.image.resize(images, size, method)

# Example usage:
# images = tf.random.normal([10, 224, 224, 3])  # 10 images of size 224x224
# resized_images = resize_images(images, [112, 112], tf.image.ResizeMethod.BILINEAR)
