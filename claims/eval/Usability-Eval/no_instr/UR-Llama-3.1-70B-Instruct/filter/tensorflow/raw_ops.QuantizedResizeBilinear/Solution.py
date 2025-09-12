# Import necessary libraries
import tensorflow as tf

# Define a function that resizes quantized images
def resize_quantized_images(images, size, min_val, max_val):
    # Use tf.raw_ops.ResizeBilinear to resize quantized images
    resized_images = tf.raw_ops.ResizeBilinear(
        images=images,
        size=size,
        min_val=min_val,
        max_val=max_val,
        Timages=tf.dtypes.float32,
        align_corners=False
    )
    return resized_images

# Create a sample input image (batch of 1 with 2 channels)
input_image = tf.constant(
    value=[[[1, 2], [3, 4]]],
    dtype=tf.float32,
    shape=(1, 2, 2, 2)  # Batch, height, width, channels
)

# Define minimum and maximum values
min_val = tf.constant(value=[0, 0], dtype=tf.float32, shape=(2,))
max_val = tf.constant(value=[255, 255], dtype=tf.float32, shape=(2,))

# Define new size for resizing
new_size = tf.constant(value=[4, 4], dtype=tf.int32, shape=(2,))

# Call the function to resize the image
resized_image = resize_quantized_images(input_image, new_size, min_val, max_val)

# Print the result
print(resized_image)
