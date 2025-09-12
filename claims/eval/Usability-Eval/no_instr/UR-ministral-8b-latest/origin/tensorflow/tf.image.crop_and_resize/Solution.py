import tensorflow as tf

def extract_and_resize_crops(image, crop_size, num_crops):
    batch_size, height, width, channels = image.shape
    crops = []

    for i in range(num_crops):
        x = i % width
        y = i // width
        crop = tf.image.crop_to_bounding_box(image, y, x, crop_size, crop_size)

        resized_crop = tf.image.resize(crop, [height, width])
        crops.append(resized_crop)

    # Stack the crops into a single tensor
    result = tf.stack(crops, axis=-1)
    return result
