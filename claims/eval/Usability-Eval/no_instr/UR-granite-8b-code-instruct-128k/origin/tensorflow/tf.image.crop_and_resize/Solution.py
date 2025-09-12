import tensorflow as tf

# Load the input image
img = tf.keras.preprocessing.image.load_img('input_image.jpg')

# Convert the image to a tensor
img_tensor = tf.keras.preprocessing.image.img_to_array(img)

# Define the size of the crops
crop_size = (100, 100)

# Define the number of crops to extract
num_crops = 10

# Extract the crops and resize them
crops = tf.image.extract_crops(img_tensor, crop_size, num_crops)
resized_crops = tf.image.resize(crops, (224, 224))

# Print the shape of the resized crops
print(resized_crops.shape)
