
import tensorflow as tf

def extract_and_resize_crops(image_tensor, num_crops, crop_size):
    image_shape = tf.shape(image_tensor)
    batch_size, image_height, image_width, num_channels = image_shape[0], image_shape[1], image_shape[2], image_shape[3]

    # Generate random crop coordinates for each crop
    crop_coords = tf.random.uniform((num_crops, 2), minval=0, maxval=image_height-crop_size, dtype=tf.int32)

    cropped_images = []
    for i in range(num_crops):
        crop_y, crop_x = crop_coords[i][0], crop_coords[i][1]
        cropped_image = tf.image.crop_to_bounding_box(image_tensor, crop_y, crop_x, crop_size, crop_size)
        cropped_image = tf.image.resize(cropped_image, (crop_size, crop_size))  # Resize crop to desired size
        cropped_images.append(cropped_image)

    return tf.stack(cropped_images)

# Example usage
input_image = tf.placeholder(tf.float32, shape=(None, 224, 224, 3))
cropped_images = extract_and_resize_crops(input_image, num_crops=5, crop_size=100)
