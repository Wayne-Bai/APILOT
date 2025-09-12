import tensorflow as tf

def crop_and_resize(input_image, boxes):
    # Crop the input image based on the specified bounding boxes
    cropped_images = []
    for box in boxes:
        x1, y1, x2, y2 = box
        cropped_image = input_image[y1:y2, x1:x2]
        cropped_images.append(cropped_image)
    
    # Resize the cropped images to the specified size
    resized_images = []
    for cropped_image in cropped_images:
        height, width = cropped_image.shape[:2]
        new_height = 256
        new_width = 256
        if height != new_height or width != new_width:
            resized_image = tf.image.resize(cropped_image, (new_height, new_width))
            resized_images.append(resized_image)
    
    return resized_images
