
import tensorflow as tf

def extract_and_resize_crops(input_image, boxes, crop_size):
    num_boxes = tf.shape(boxes)[0]
    cropped_images = []
    
    for i in range(num_boxes):
        box = boxes[i]
        crop = tf.image.crop_to_bounding_box(input_image, box[0], box[1], box[2], box[3])
        resized_crop = tf.image.resize(crop, crop_size)
        cropped_images.append(resized_crop)
    
    return tf.stack(cropped_images)

# Example usage
input_image = tf.placeholder(tf.float32, shape=(None, None, 3))  # Assume RGB image
boxes = tf.constant([[0, 0, 50, 50], [20, 30, 70, 80]])  # Example bounding boxes
crop_size = [30, 30]  # Target size of the crops

output = extract_and_resize_crops(input_image, boxes, crop_size)
