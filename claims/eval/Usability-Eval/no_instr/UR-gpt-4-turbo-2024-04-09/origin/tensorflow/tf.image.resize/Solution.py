import tensorflow as tf

def resize_image(image, target_height, target_width, method='bilinear'):
    # Convert the image to a tensor
    image_tensor = tf.convert_to_tensor(image)
    # Add batch dimension
    image_tensor = image_tensor[tf.newaxis, ...]
    # Resize image
    resized_image = tf.image.resize(image_tensor, [target_height, target_width], method=method)
    # Remove batch dimension
    resized_image = resized_image[0]
    return resized_image

# Example usage
# Load image file
image_path = 'path_to_image.jpg'
image_raw = tf.io.read_file(image_path)
image = tf.image.decode_image(image_raw)

# Resize image to 300x300 using bilinear method
resized_image = resize_image(image, 300, 300, method='bilinear')
