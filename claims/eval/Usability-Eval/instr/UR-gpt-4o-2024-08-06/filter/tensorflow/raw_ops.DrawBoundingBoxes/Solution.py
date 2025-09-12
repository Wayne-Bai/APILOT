import tensorflow as tf
import matplotlib.pyplot as plt

def draw_bounding_boxes(images, boxes):
    """
    Draw bounding boxes on a batch of images.

    Parameters:
    - images: A 4-D tensor of shape [batch, height, width, channels].
    - boxes: A 3-D tensor of shape [batch, num_boxes, 4].
             Each box is defined by [y_min, x_min, y_max, x_max] with values between [0, 1].
    """
    # Assume images are batched in NHWC format
    batch_size = tf.shape(images)[0]
    num_boxes = tf.shape(boxes)[1]

    for i in range(batch_size):
        image = images[i]
        plt.imshow(image.numpy())
        
        for j in range(num_boxes):
            y_min, x_min, y_max, x_max = boxes[i][j].numpy()
            image_height, image_width, _ = image.shape
            
            # Rescale box coordinates to image size
            y_min = int(y_min * image_height)
            x_min = int(x_min * image_width)
            y_max = int(y_max * image_height)
            x_max = int(x_max * image_width)

            # Draw rectangle
            plt.gca().add_patch(plt.Rectangle((x_min, y_min), x_max - x_min, y_max - y_min,
                                               fill=False, edgecolor='red', linewidth=2))
        plt.show()

# Example usage
batch_size = 2
height, width = 128, 128
channels = 3
num_boxes = 2

# Randomly generate a batch of images and bounding boxes
images = tf.random.uniform(shape=[batch_size, height, width, channels], minval=0, maxval=1)
boxes = tf.random.uniform(shape=[batch_size, num_boxes, 4], minval=0, maxval=1)

draw_bounding_boxes(images, boxes)
