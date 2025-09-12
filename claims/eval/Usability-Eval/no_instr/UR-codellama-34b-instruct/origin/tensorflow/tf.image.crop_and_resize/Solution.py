import tensorflow as tf

# Load the input image tensor
image = tf.io.read_file("input_image.jpg")

# Define the size of the cropped images
crop_size = (224, 224)

# Extract crops from the input image
crops = tf.image.extract_crops(image, crop_size)

# Resize the crops to the desired size
resized_crops = [tf.image.resize(crop, (299, 299)) for crop in crops]

# Print the shape of the resized crops
print("Shape of resized crops:", resized_crops[0].shape)
