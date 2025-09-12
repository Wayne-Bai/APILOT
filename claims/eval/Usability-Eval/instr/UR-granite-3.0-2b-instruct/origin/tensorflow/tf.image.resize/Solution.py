import tensorflow as tf
from PIL import Image
import numpy as np

def resize_image(image_path, output_size):
    # Open the image file
    img = Image.open(image_path)

    # Convert the image to a numpy array
    img_array = np.array(img)

    # Reshape the image array to have a shape of (height, width, channels)
    img_array = img_array.reshape((img_array.shape[0], img_array.shape[1], 3))

    # Resize the image array using the specified method
    resized_img = tf.image.resize(img_array, [output_size, output_size])

    # Convert the resized image array back to a PIL image
    resized_img = resized_img.numpy().astype(np.uint8)
    resized_img = Image.fromarray(resized_img)

    # Save the resized image to a file
    resized_img.save('resized_image.jpg')

# Example usage
resize_image('input_image.jpg', 256)
