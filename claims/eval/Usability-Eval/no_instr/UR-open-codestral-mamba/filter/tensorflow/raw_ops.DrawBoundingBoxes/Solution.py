import tensorflow as tf
import matplotlib.pyplot as plt

def draw_boxes(images, boxes, color, line_width=3):
    # Convert images to float type
    images = tf.cast(images, tf.float32)

    # Get the dimensions of the images
    batch_size, height, width, _ = images.get_shape().as_list()
    image_dims = tf.cast(tf.stack([height, width, width, 1]), tf.float32)

    # Define colors
    colors = tf.constant(color, dtype=tf.float32)

    # Normalize coordinates of bounding boxes
    boxes = tf.reshape(boxes, [-1, 4])
    boxes = tf.divide(boxes, image_dims)

    # Extract coordinates of bounding boxes
    y1, x1, y2, x2 = tf.split(boxes, 4, axis=1)

    # Create coordinate grid for image
    x, y = tf.meshgrid(tf.range(width), tf.range(height))
    coords = tf.cast(tf.stack([y, x], axis=2), tf.float32)

    # Check if coordinates are within bounding boxes
    in_boxes = tf.logical_and(tf.logical_and(tf.logical_and(y1 * height <= coords[:, :, 0], coords[:, :, 0] <= y2 * height),
                                              tf.logical_and(x1 * width <= coords[:, :, 1], coords[:, :, 1] <= x2 * width)))

    # Change the color of pixels within bounding boxes
    new_colors = tf.where(in_boxes, colors, tf.zeros_like(colors))
    new_colors = tf.expand_dims(new_colors, axis=0)
    new_colors = tf.tile(new_colors, [batch_size, 1, 1, 1])

    # Apply color change to images
    images = tf.where(tf.equal(new_colors, colors), colors, images)

    return images

def plot_images(images):
    # Plot images
    fig, axes = plt.subplots(1, len(images), figsize=(15, 15))
    for ax, image in zip(axes, images):
        ax.imshow(image.astype("uint8"))
        ax.set_axis_off()

    plt.show()

# Load a single image
image = tf.image.decode_jpeg(tf.io.read_file("path_to_your_image.jpg"), channels=3)
batch_images = tf.expand_dims(image, axis=0)

# Define bounding box and color
y1, x1, y2, x2 = 0.2, 0.3, 0.7, 0.8
boxes = tf.constant([y1, x1, y2, x2], shape=(1, 4), dtype=tf.float32)
color = tf.constant([255, 0, 0], shape=(3,), dtype=tf.float32)

# Draw bounding boxes and plot image
top_image = draw_boxes(batch_images, boxes, color)
plot_images(top_image)
