import tensorflow as tf

def resize_quantized_image(image, size):
    # Ensure the input image is quantized to the expected range
    if image.dtype != tf.uint8:
        raise ValueError("Image should be of type tf.uint8 for quantized images")
    
    # Resize using tf.image.resize with image resizing following quantized bilinear interpolation
    resized_image = tf.image.resize(image, size, method='bilinear')
    
    return tf.quantization.quantize(resized_image, 
                                     min_value=0.0, 
                                     max_value=255.0, 
                                     T=tf.uint8, 
                                     mode='SCALED')

# Example usage
image = tf.constant([[255, 0], [255, 0]], dtype=tf.uint8)
size = (4, 4)
resized_image = resize_quantized_image(image, size)
tf.print(resized_image)
