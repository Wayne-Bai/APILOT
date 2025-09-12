import tensorflow as tf
from tensorflow.keras.applications.resnet50 import preprocess_input
from tensorflow.keras.preprocessing import image

def extract_crops(input_image, crop_sizes):
    input_image = preprocess_input(input_image)
    crops = []

    for size in crop_sizes:
        crop = input_image.crop((size, size, size+input_image.shape[1], size+input_image.shape[0]))
        crops.append(tf.image.resize(crop, (size, size)))

    return crops

# Example usage:
# Load an image
img_path = 'path_to_your_image.jpg'
img = image.load_img(img_path, target_size=(224, 224))

# Preprocess the image
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

# Define crop sizes
crop_sizes = [100, 200, 300]

# Extract crops
crops = extract_crops(x, crop_sizes)

# Print the crops
for i, crop in enumerate(crops):
    print(f'Crop {i+1}:')
    print(crop)
