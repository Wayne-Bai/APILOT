import tensorflow as tf

# Define the input image
input_image = tf.image.decode_jpeg(tf.io.read_file('input.jpg'), channels=3)

# Define the desired image size
desired_size = (224, 224)  # Replace with your desired size

# Resize the image
resized_image = tf.image.resize(input_image, desired_size)

# Print the shape of the resized image
print("Resized image shape:", resized_image.shape)
