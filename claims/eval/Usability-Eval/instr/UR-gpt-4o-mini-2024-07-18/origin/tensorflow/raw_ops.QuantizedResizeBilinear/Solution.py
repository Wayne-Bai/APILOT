import tensorflow as tf

def resize_quantized_images(images, size, method='bilinear'):
    # Ensure images are of type tf.uint8
    images = tf.convert_to_tensor(images, dtype=tf.uint8)
    
    # Resize quantized images using bilinear interpolation
    resized_images = tf.image.resize(images, size, method=method)
    
    return resized_images

# Example usage:
# images = tf.random.uniform(shape=[1, 100, 100, 3], minval=0, maxval=256, dtype=tf.int32)
# resized_images = resize_quantized_images(images, size=[200, 200])
