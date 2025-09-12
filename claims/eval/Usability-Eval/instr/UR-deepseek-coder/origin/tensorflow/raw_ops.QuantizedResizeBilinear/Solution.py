import tensorflow as tf

def resize_quantized_images(images, size, method='bilinear', align_corners=False):
    # Convert images to float32 for resizing
    images_float = tf.cast(images, tf.float32)
    
    # Perform the resizing using bilinear interpolation
    resized_images_float = tf.image.resize(images_float, size, method=method, align_corners=align_corners)
    
    # Quantize the resized images back to the original data type
    resized_images = tf.cast(resized_images_float, images.dtype)
    
    return resized_images

# Example usage:
# images = ...  # Your quantized image tensor (e.g., tf.uint8)
# new_size = [new_height, new_width]
# resized_images = resize_quantized_images(images, new_size)
