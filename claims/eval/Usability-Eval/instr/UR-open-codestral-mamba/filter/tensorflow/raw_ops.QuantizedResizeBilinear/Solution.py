import tensorflow as tf

def resize_quantized_images(images, new_size):
    images_resized = tf.image.resize(images, new_size, method=tf.image.ResizeMethod.BILINEAR)
    return images_resized

# Test the function
images = tf.random.uniform([10, 20, 20, 3], minval=0, maxval=255, dtype=tf.dtypes.quint8)
new_size = (40, 40)
images_resized = resize_quantized_images(images, new_size)

print("Original Images Shape:", images.shape)
print("Resized Images Shape:", images_resized.shape)
