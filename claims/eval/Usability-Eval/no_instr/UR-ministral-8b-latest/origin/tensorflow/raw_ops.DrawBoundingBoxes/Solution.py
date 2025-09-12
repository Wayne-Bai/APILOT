import tensorflow as tf

def draw_bounding_boxes(images, bounding_boxes):
    """
    Draw bounding boxes on a batch of images.

    Parameters:
    images (tf.Tensor): A batch of input images, shape [batch_size, height, width, channels].
    bounding_boxes (tf.Tensor): A tensor of bounding boxes, shape [batch_size, num_boxes, 4],
                               where 4 is [top_x, top_y, bottom_x, bottom_y].

    Returns:
    tf.Tensor: A tensor of images with drawn bounding boxes.
    """

    def draw_box(image, bbox):
        # Extract the bounding box coordinates
        top_x, top_y, bottom_x, bottom_y = bbox

        # Convert the bounding box coordinates to integer for drawing
        top_x, top_y, bottom_x, bottom_y = int(top_x), int(top_y), int(bottom_x), int(bottom_y)

        # Draw a rectangular bounding box on the image
        image = tf.image.draw_bounding_box(image, [top_y, bottom_y, top_x, bottom_x], [1, 1, 1, 1], image_shape=image.shape[-4:])
        return image

    # Apply draw_box function to each image and its corresponding bounding box
    images_with_boxes = tf.map_fn(lambda img, box: draw_box(img, box), (images, bounding_boxes))

    return images_with_boxes

# Example usage:
input_images = tf.random.uniform(shape=[2, 64, 64, 3])
bounding_boxes = tf.random.uniform(shape=[2, 2, 4])
output_images = draw_bounding_boxes(input_images, bounding_boxes)

print(output_images)
