import tensorflow as tf

def resize_quantized_images(images, size, align_corners=False, half_pixel_centers=False):
    # Ensure the images are in quantized format
    if images.dtype != tf.uint8:
        raise ValueError("Input images must be of type tf.uint8")

    resized_images = tf.image.resize(images, size, method='bilinear', 
                                      align_corners=align_corners,
                                      half_pixel_centers=half_pixel_centers)
    
    return tf.cast(resized_images, tf.uint8)

# Example usage
# images = tf.constant([...], dtype=tf.uint8)  # Input your quantized image here
# size = (height, width)  # New size
# resized_images = resize_quantized_images(images, size)
