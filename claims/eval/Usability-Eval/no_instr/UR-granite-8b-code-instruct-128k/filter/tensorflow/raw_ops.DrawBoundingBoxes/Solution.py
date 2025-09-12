import tensorflow as tf

# Assuming you have a batch of images and their bounding boxes
images = ...
bboxes = ...

# Define the bounding box drawing function
def draw_bounding_box(image, bbox):
    x1, y1, x2, y2 = bbox
    image = tf.image.draw_bounding_boxes(tf.expand_dims(image, 0), [tf.expand_dims(tf.stack([y1, x1, y2, x2]), 0)])
    return image

# Iterate over the images and bounding boxes and draw bounding boxes
drawn_images = []
for image, bbox in zip(images, bboxes):
    drawn_image = draw_bounding_box(image, bbox)
    drawn_images.append(drawn_image)

# Stack the drawn images together to form a batch
batch = tf.stack(drawn_images)
