import tensorflow as tf
from tensorflow.python.ops import math_ops
from tensorflow.python.ops import array_ops

# Define the input image and new size
image = tf.random.uniform((256, 256, 3))
new_size = (128, 128)

# Define the quantization parameters
quantization = tf.int32

# Define the mode for resizing (NEAREST_NEIGHBOR, BILINEAR, AREA, CUBIC, CUBIC_EXT, LANCZOS3)
mode = tf.controls.ResizeMethod.BILINEAR

# Use tf.image.resize_bilinear for bilinear interpolation
resized_image = tf.image.resize_bilinear(image,
                                         array_ops.concat([(tf.constant(new_size, dtype=tf.int32))],
                                      0))

# Use tf.cast and tf(ImageQuantize) for quantization
quantized_image = tf.image.resize_bilinear(tf.cast(image, quantization),
                                       array_ops.concat([(tf.constant(new_size, dtype=tf.int32))], 0))
quantized_image = tf.quantization.image_quantize(quantized_image,
        
    # Pass zero point  and quantization scale to quantize image
    quantized_image, 0, 4        
    )
# Merge the resized image and data in TensorFlow tensor tf.Print.
# tf.Print: helper function to print a dialog inside TensorFlow.
with tf.Print(
    resized_image,
    [quantized_image],
    message='Quantized Image:'):
    pass
