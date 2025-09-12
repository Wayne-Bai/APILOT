import tensorflow as tf

def resize_quantized_images(images, size):
    # Ensure that the input images are of type tf.uint8
    images = tf.convert_to_tensor(images, dtype=tf.uint8)
    
    # Resize images using quantized bilinear interpolation
    resized_images = tf.image.resize(images, size, method='bilinear')
    
    return resized_images

# Example usage:
# images = tf.constant([[[[255, 0, 0], [0, 255, 0]], [[0, 0, 255], [255, 255, 0]]]], dtype=tf.uint8)
# size = [4, 4]
# resized = resize_quantized_images(images, size)
# print(resized)
