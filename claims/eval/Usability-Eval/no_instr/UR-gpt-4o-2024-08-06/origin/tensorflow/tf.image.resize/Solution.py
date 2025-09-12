import tensorflow as tf

# Function to resize images
def resize_image(image_path, target_size=(256, 256), resize_method='bilinear'):
    # Load the image
    image = tf.io.read_file(image_path)
    image = tf.image.decode_image(image, channels=3)
    
    # Resize the image
    resized_image = tf.image.resize(image, target_size, method=resize_method)
    
    return resized_image

# Example usage
# Assuming you have a path to an image file
image_path = 'path/to/your/image.jpg'
resized_image = resize_image(image_path, target_size=(256, 256), resize_method='bilinear')

# Convert the tensor to an image and save it
resized_image = tf.cast(resized_image, tf.uint8)
resized_image = tf.image.encode_jpeg(resized_image)
tf.io.write_file('path/to/save/resized_image.jpg', resized_image)
