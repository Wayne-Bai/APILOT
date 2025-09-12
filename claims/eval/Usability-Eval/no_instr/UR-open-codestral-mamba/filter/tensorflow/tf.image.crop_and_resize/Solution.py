import tensorflow as tf

def extract_and_resize_crops(image, crops_coords, crop_size, resize_shape):
    extracted_crops = []
    for coord in crops_coords:
        # Extract crop
        crop = tf.image.crop_to_bounding_box(image, coord[0], coord[1], coord[2], coord[3])
        # Resize crop
        resize_crop = tf.image.resize(crop, resize_shape)
        extracted_crops.append(resize_crop)
    return tf.stack(extracted_crops)
