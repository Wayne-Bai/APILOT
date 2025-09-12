# Import necessary libraries
import tensorflow as tf
import numpy as np

# Define a function to draw bounding boxes
def draw_bounding_boxes(image, boxes, line_thickness=1):
    # Convert the image to a tensor
    image = tf.convert_to_tensor(image)

    # Convert the boxes to a tensor
    boxes = tf.convert_to_tensor(boxes)

    # Create a tensor to store the drawn image
    drawn_image = tf.zeros_like(image)

    # Draw the bounding boxes on the new image
    for box in boxes:
        # Get the coordinates of the box
        ymin, xmin, ymax, xmax = tf.unstack(box)

        # Draw the boundary
        boundary = tf.stack([
            [ymin, xmin],
            [ymin, xmax],
            [ymax, xmax],
            [ymax, xmin],
            [ymin, xmin]
        ], axis=1)

        # Draw the boundary on the new image
        drawn_image = tf.tensor_scatter_nd_update(
            drawn_image, [(i, j) for i in tf.range(ymin, ymax) for j in tf.range(xmin, xmax)],
            tf.ones([(ymax-ymin)*(xmax-xmin)], dtype=image.dtype) * tf.constant(line_thickness)
        )

        # Draw the box on the new image
        drawn_image = tf.tensor_scatter_nd_update(
            drawn_image, [(i, j) for i in tf.range(ymin, ymax) for j in tf.range(xmin, xmax)],
            tf.ones([(ymax-ymin)*(xmax-xmin)], dtype=image.dtype)
        )

    return drawn_image

# Create some random images and boxes
np.random.seed(0)
images = (np.random.rand(10, 256, 256, 3) * 255).astype(np.uint8)
boxes = np.random.rand(10, 4).astype(np.float32)

# Draw the bounding boxes on the images
drawn_images = [draw_bounding_boxes(image, box) for image, box in zip(images, boxes)]

# Print the drawn images
for i, image in enumerate(drawn_images):
    print(f"Image {i} shape: {image.shape}")

# Save the drawn images to disk
for i, image in enumerate(drawn_images):
    tf.keras.preprocessing.image.save_img(f'img_{i}.png', image.astype(np.uint8))
