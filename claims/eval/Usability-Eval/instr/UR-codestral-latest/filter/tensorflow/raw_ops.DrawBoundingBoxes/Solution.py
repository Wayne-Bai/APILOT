import tensorflow as tf

# Assume we have a batch of images and a corresponding batch of bounding boxes
# Images shape: (batch_size, height, width, channels)
# Bounding boxes shape: (batch_size, num_boxes, 4) with boxes in [y1, x1, y2, x2] format
images = tf.random.uniform((10, 200, 200, 3))
boxes = tf.random.uniform((10, 5, 4))

# Normalize boxes to be between 0 and 1 by dividing by the image size
image_size = tf.cast(tf.shape(images)[1:3], tf.float32)
boxes = tf.divide(boxes, tf.tile(image_size, [1, 2]))

# Draw bounding boxes on the images
images_with_boxes = tf.image.draw_bounding_boxes(images, boxes)
