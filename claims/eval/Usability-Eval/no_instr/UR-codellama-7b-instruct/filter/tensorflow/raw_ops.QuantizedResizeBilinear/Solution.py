
import tensorflow as tf

def resize_quantized_images(images, size):
    # Get the shape of the input images
    image_shape = tf.shape(images)
    
    # Compute the scale factor for each dimension
    scale_factor = [size[i] / image_shape[i] for i in range(len(image_shape))]
    
    # Create a bilinear interpolation kernel
    kernel = tf.constant([[1, 2, 1], [2, 4, 2], [1, 2, 1]]) / 4
    
    # Apply the kernel to each dimension of the input images
    output_images = []
    for i in range(len(image_shape)):
        output_images.append(tf.nn.depthwise_conv2d(images[:, :, :, i], kernel, strides=[1, 1, 1, 1], padding='SAME'))
    
    # Resize the images to the specified size
    output_images = tf.concat(output_images, axis=-1)
    output_images = tf.image.resize_nearest_neighbor(output_images, size)
    
    return output_images
