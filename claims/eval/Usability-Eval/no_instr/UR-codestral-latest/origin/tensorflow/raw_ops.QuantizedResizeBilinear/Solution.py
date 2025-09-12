import tensorflow as tf

# Define an example quantized image
quantized_image = tf.random.uniform([1, 10, 10, 1], minval=0, maxval=255, dtype=tf.qint32)

# Define the new size for the image
new_size = [20, 20]

# Resize the quantized image
resized_image = tf.image.resize(quantized_image, new_size, method='bilinear')

# Convert the resized image back to uint8 data type
resized_image = tf.cast(resized_image, tf.uint8)

# Print the shapes of the original and resized images
print("Shape of original quantized image:", quantized_image.shape)
print("Shape of resized quantized image:", resized_image.shape)
