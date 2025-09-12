import tensorflow as tf

# Define the image shape and resizing method
image_shape = (28, 28, 3) # RGB image with height=28, width=28
method = "bilinear"

# Load the input image
image = ... # Replace with your image loading logic

# Resize the image using the specified method
resized_image = tf.image.resize(image, image_shape, method)

# Print the resized image
print(resized_image)
