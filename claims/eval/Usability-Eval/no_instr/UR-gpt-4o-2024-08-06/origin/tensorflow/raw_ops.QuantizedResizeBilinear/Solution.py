import tensorflow as tf

# Function to resize quantized images using bilinear interpolation
def resize_quantized_images(input_image, size):
    # Ensure that the input is a quantized tensor, typically tf.quint8 or tf.qint32
    input_min = tf.reduce_min(input_image)
    input_max = tf.reduce_max(input_image)

    # Resize the image using tf.image.resize which uses bilinear interpolation by default
    resized_image = tf.image.resize(input_image, size, method='bilinear')

    # Convert the resized image back to the quantized format using the input range
    quantized_resized_image = tf.quantization.quantize(resized_image, input_min, input_max, tf.qint32)
    
    return quantized_resized_image

# Example usage
input_image = tf.constant([[1, 2], [3, 4]], dtype=tf.qint32)
size = (300, 300)

resized_image = resize_quantized_images(input_image, size)

print(resized_image)
