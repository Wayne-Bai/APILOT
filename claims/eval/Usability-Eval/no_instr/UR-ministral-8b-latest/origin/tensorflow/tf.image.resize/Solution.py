import tensorflow as tf
from PIL import Image

def resize_image(image_path, target_size):
    # Load the image using PIL
    img = Image.open(image_path)

    # Resize the image using PIL
    img_resized = img.resize(target_size)

    # Convert the PIL image back to a NumPy array
    img_array = tf.convert_to_tensor(img_resized)

    return img_array

# Example usage
image_path = 'path/to/your/image.jpg'
target_size = (256, 256)  # Replace with your desired target size
resized_image = resize_image(image_path, target_size)
