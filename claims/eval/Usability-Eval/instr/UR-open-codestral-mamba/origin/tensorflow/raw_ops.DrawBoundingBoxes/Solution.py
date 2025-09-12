import tensorflow as tf

def draw_bounding_boxes(images, boxes, labels):
    """Draw bounding boxes on a batch of images.

    Args:
        images: A float32 tensor of shape [batch_size, height, width, channels].
        boxes: A float32 tensor of shape [batch_size, N, 4] containing the coordinates of the bounding boxes.
            The coordinates should be normalized (i.e., the y and x coordinates of the origin and the dimensions
            of the bounding box should be between 0 and 1).
        labels: A int32 tensor of shape [batch_size, N] containing the labels of the bounding boxes.

    Returns:
        A float32 tensor of shape [batch_size, height, width, channels] containing the input images with bounding boxes drawn on them.
    """
    # Define colors for each label
    colormap = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

    # Reshape images to [batch_size * height * width * channels]
    images_flat = tf.reshape(images, [-1])

    # Get coordinates and dimensions of bounding boxes
    ys, xs, hs, ws = tf.unstack(boxes, axis=2)

    # Iterate over batch
    for i in range(tf.shape(images)[0]):
        # Get bounding boxes and labels for current image
        boxes_i = boxes[i]
        labels_i = labels[i]

        # Iterate over bounding boxes for current image
        for j in range(tf.shape(boxes_i)[0]):
            # Get coordinates, dimensions and label of current bounding box
            y, x, h, w = tf.unstack(boxes_i[j])
            label = labels_i[j]

            # Scale coordinates and dimensions according to images it corresponds to
            y = tf.cast(y * tf.cast(tf.shape(images)[1], tf.float32), tf.int32)
            x = tf.cast(x * tf.cast(tf.shape(images)[2], tf.float32), tf.int32)
            h = tf.cast(h * tf.cast(tf.shape(images)[1], tf.float32), tf.int32)
            w = tf.cast(w * tf.cast(tf.shape(images)[2], tf.float32), tf.int32)

            # Set bounding box pixels
            for row in range(y, y+h+1):
                start = (row * tf.shape(images)[2] + x) * tf.shape(images)[3]
                end = start + w
                images_flat[start:end].assign(tf.constant(colormap[label], tf.float32))

    # Reshape images_flat back to [batch_size, height, width, channels] and return
    result = tf.reshape(images_flat, [tf.shape(images)[0], tf.shape(images)[1], tf.shape(images)[2], tf.shape(images)[3]])
    return result
