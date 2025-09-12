import tensorflow as tf

def resize_image(image_path, new_size):
    # Load the image file
    image = tf.io.read_file(image_path)

    # Decode the image
    image_tensor = tf.image.decode_image(image, channels=3)

    # Resize the image
    resized_image = tf.image.resize(image_tensor, new_size)

    return resized_image

# Testing the function
input_image_path = "path_to_your_image_file"
new_image_size = (200, 200)

resized_image = resize_image(input_image_path, new_image_size)
print(resized_image)
