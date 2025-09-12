import tensorflow as tf

# Function to draw bounding boxes on images
def draw_bounding_boxes(images, bounding_boxes, colors=(255, 0, 0)):
    """
    images: A batch of images
    bounding_boxes: A batch of bounding boxes with shape (batch_size, num_boxes, 4)
    colors: A tuple representing the color of the bounding boxes
    """
    batch_size = tf.shape(images)[0]
    num_boxes = tf.shape(bounding_boxes)[1]

    # Initialize images for drawing bounding boxes
    images_with_boxes = images

    for i in range(batch_size):
        for j in range(num_boxes):
            # Extract ymin, xmin, ymax, xmax from bounding boxes
            ymin, xmin, ymax, xmax = tf.unstack(bounding_boxes[i, j])
            # Convert coordinates to integers
            ymin = tf.cast(ymin, tf.int32)
            xmin = tf.cast(xmin, tf.int32)
            ymax = tf.cast(ymax, tf.int32)
            xmax = tf.cast(xmax, tf.int32)

            # Extract image and use non-zero color for drawing boxes
            image = images_with_boxes[i]
            for k in range(3):  # Loop over color channels
                image_with_boxes = image[:, ymin:ymax, k]
                image_with_boxes.row1 = tf.where(image_with_boxes <= 0, 0, image_with_boxes)
                image_with_boxes = tf.where(xmin <= tf.add(image_with_boxes, tf.fill(tf.shape(image_with_boxes), ymin), 0) == 0, 255, image_with_boxes)
                image_with_boxes = tf.where(xmax >= tf.add(image_with_boxes, tf.fill(tf.shape(image_with_boxes), xmax), 0) == 0, 255, image_with_boxes)

            # Combine and update images with boxes
            images_with_boxes[i, :, :, k] = tf.add(image_with_boxes, tf.cast(colors[k], tf.float32))

    return images_with_boxes
