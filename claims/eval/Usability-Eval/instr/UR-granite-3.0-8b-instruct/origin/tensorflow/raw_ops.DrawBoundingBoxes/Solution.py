import tensorflow as tf

# Assuming you have a batch of images and bounding boxes
images = tf.placeholder(tf.float32, shape=(None, None, None, 3))
bboxes = tf.placeholder(tf.float32, shape=(None, None, 4))

# Define the colors for the bounding boxes
colors = [(0, 0, 255), (0, 255, 0), (255, 0, 0), (255, 255, 0), (0, 255, 255), (255, 0, 255), (255, 255, 255), (0, 0, 0)]

# Define a function to draw bounding boxes
def draw_bounding_boxes(image, bboxes):
    for i in range(bboxes.shape[0]):
        x1, y1, x2, y2 = bboxes[i]
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        image = tf.image.draw_bounding_boxes(image, [tf.constant([x1, y1, x2, y2])], colors[i % len(colors)])
    return image

# Draw bounding boxes on the images
drawn_images = draw_bounding_boxes(images, bboxes)
