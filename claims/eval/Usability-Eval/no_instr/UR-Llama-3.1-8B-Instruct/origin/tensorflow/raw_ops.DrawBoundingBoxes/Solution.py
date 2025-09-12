import tensorflow as tf
from tensorflow import io
import numpy as np

# Load an image
image_path = "path_to_your_image.jpg"
image = io.read_file(image_path)
image = tf.image.decode_jpeg(image, channels=3)
image = tf.image.resize(image, (512, 512))

# Create some bounding boxes
num_boxes = 10
box_coords = np.zeros((num_boxes, 4), dtype=np.float32)
box_coords[:, 2:] = 50.0  # width and height
box_classes = np.full((num_boxes,), 1, dtype=np.int32)  # set all classes to 1

# Convert numpy arrays to tensors
box_coords = tf.convert_to_tensor(box_coords)
box_classes = tf.convert_to_tensor(box_classes)

# Draw bounding boxes on the image
image_with_boxes = tf.image.draw_bounding_boxes(image, boxes=tf.expand_dims(box_coords, axis=0), classes=tf.expand_dims(box_classes, axis=0))

# Save the image with bounding boxes
with tf.io.gfile.GFile("image_with_boxes.jpg", "wb") as f:
  f.write(tf.image.encode_jpeg(image_with_boxes))
