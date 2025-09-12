import tensorflow as tf

def draw_bounding_boxes(images, boxes, colors):
    """
    Draw bounding boxes on a batch of images.

    Args:
        images (tf.Tensor): A batch of images with shape (batch_size, height, width, channels)
        boxes (tf.Tensor): A batch of bounding boxes with shape (batch_size, num_boxes, 4)
        colors (tf.Tensor): A batch of colors with shape (batch_size, num_boxes, 3)

    Returns:
        tf.Tensor: Images with bounding boxes drawn on them
    """
    # Convert images to float32
    images = tf.cast(images, tf.float32)

    # Loop over each image and its corresponding boxes and colors
    drawn_images = []
    for image, box, color in zip(images, boxes, colors):
        # Loop over each box and its corresponding color
        for b, c in zip(box, color):
            # Draw the bounding box on the image
            image = tf.raw_ops.DrawBoundingBoxes(
                image=image,
                boxes=b[tf.newaxis, :],
                colors=c[tf.newaxis, :]
            )

        drawn_images.append(image)

    # Stack the drawn images into a batch
    drawn_images = tf.stack(drawn_images)

    return drawn_images

# Example usage:
if __name__ == "__main__":
    # Define a batch of images
    images = tf.random.uniform((4, 256, 256, 3))

    # Define a batch of bounding boxes
    boxes = tf.random.uniform((4, 10, 4))

    # Define a batch of colors
    colors = tf.random.uniform((4, 10, 3))

    # Draw the bounding boxes on the images
    drawn_images = draw_bounding_boxes(images, boxes, colors)

    # Print the shape of the drawn images
    print(drawn_images.shape)
