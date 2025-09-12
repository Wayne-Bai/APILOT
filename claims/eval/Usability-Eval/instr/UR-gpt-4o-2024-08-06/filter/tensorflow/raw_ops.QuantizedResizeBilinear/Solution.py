import tensorflow as tf

def quantized_resize_bilinear(images, size, input_min, input_max, align_corners=False):
    """
    Resize quantized images using bilinear interpolation with target size.
    
    Parameters:
    - images: A 4-D tensor of shape `[batch, height, width, channels]` with quantized image data.
    - size: A 1-D tensor of 2 elements: `new_height, new_width`. The new size for the images.
    - input_min: A float that represents the min value for the quantized range.
    - input_max: A float that represents the max value for the quantized range.
    - align_corners: An optional bool. Defaults to False. If True, the centers of 
      the 4 corner pixels of the input and output tensors are aligned, preserving the values at 
      the corner pixels.
    
    Returns:
    - A tuple of tensors `(resized_images, output_min, output_max)`.
      resized_images: A 4-D tensor of shape `[batch, new_height, new_width, channels]`.
      output_min and output_max: Float values for the new quantized range.
    """
    # Dequantize the input images into float32
    images_float = tf.quantization.dequantize(images, input_min, input_max, mode='SCALED')

    # Resize the images using bilinear interpolation
    resized_images_float = tf.image.resize(images_float, size, method=tf.image.ResizeMethod.BILINEAR, align_corners=align_corners)

    # Re-quantize the resized images to the quantized range
    resized_images, output_min, output_max = tf.quantization.quantize(resized_images_float, input_min, input_max, tf.qint8)

    return resized_images, output_min, output_max

# Example usage
# Assuming `quantized_images` is a 4-D tensor with shape `[batch, height, width, channels]`
# and `input_min` and `input_max` are the quantized range for `quantized_images`.
quantized_images = tf.random.uniform([1, 100, 100, 3], minval=0, maxval=255, dtype=tf.int32)
quantized_images = tf.cast(quantized_images, tf.qint8)
input_min, input_max = 0.0, 255.0

new_size = [50, 50]
resized_images, output_min, output_max = quantized_resize_bilinear(quantized_images, new_size, input_min, input_max)
print(resized_images, output_min, output_max)
