import tensorflow as tf
from PIL import Image
import numpy as np

def resize_image(image_path, output_size):
    # Open the image file
    img = Image.open(image_path)

    # Convert the image to a numpy array
    img_array = np.array(img)

    # Define the target shape
    target_shape = (output_size, output_size)

    # Resize the image
    resized_img = tf.image.resize(img_array, target_shape)

    # Save the resized image
    resized_img = resized_img.numpy()
    resized_img = (resized_img * 255).astype(np.uint8)
    resized_img = Image.fromarray(resized_img)
    resized_img.save('resized_image.jpg')

# Example usage
resize_image('input_image.jpg', 256)
