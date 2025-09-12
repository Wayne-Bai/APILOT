import tensorflow as tf

# Load the image
img = tf.io.read_file('path/to/image.jpg')
img = tf.image.decode_image(img, channels=3)

# Resize the image
resized_img = tf.image.resize(img, [224, 224])

# Display the resized image
tf.imshow(resized_img)
tf.show()
