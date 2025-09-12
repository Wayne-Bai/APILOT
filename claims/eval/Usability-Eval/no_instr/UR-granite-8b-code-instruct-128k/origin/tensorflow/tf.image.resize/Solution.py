
import tensorflow as tf

# Load the image
img = tf.keras.utils.load_img('path_to_image.jpg', target_size=(256, 256))

# Convert the image to a tensor
img_tensor = tf.keras.utils.img_to_array(img)

# Resize the image using the specified method
resized_img = tf.image.resize(img_tensor, (256, 256), method='bilinear')

# Display the resized image
tf.keras.utils.plot_img(resized_img)
