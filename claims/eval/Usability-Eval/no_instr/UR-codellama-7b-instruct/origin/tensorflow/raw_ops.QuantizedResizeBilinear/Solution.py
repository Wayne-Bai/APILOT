
import tensorflow as tf

# Define the input and output sizes
input_size = (256, 256)
output_size = (128, 128)

# Load the quantized images
image_paths = ["path/to/image1.jpg", "path/to/image2.jpg"]
images = [tf.io.decode_jpeg(tf.io.read_file(image_path), channels=3) for image_path in image_paths]

# Resize the images using quantized bilinear interpolation
resized_images = tf.resize(images, size=output_size, method="QUANTIZED", align_corners=False)
