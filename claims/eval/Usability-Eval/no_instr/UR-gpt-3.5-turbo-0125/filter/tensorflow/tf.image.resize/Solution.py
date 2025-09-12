
import tensorflow as tf

def resize_images(images, method='bilinear', size=(224,224)):
    # Reshape images to 4D tensor
    images = tf.expand_dims(images, 0)
    
    # Resize images based on the specified method
    resized_images = tf.image.resize(images, size, method=method)
    
    return tf.squeeze(resized_images, 0)

# Usage example
images = tf.constant([[[[1.0, 2.0], [3.0, 4.0]]]])  # Example image tensor
resized_images = resize_images(images, method='bilinear', size=(224,224))
