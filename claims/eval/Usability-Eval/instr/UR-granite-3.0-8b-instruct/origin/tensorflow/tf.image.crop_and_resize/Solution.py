import tensorflow as tf

def extract_and_resize_crops(image, boxes, output_size):
    # Extract crops from the input image tensor
    crops = tf.image.crop_to_bounding_boxes(image, boxes)

    # Resize the extracted crops to the desired output size
    resized_crops = tf.image.resize(crops, output_size)

    return resized_crops
