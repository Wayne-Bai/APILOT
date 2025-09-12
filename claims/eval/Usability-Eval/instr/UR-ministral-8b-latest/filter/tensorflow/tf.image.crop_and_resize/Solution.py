import tensorflow as tf

def crop_and_resize(image_tensor, crop_height, crop_width, target_height, target_width):
    # Crop the image tensor
    croped_tensor = tf.image.crop_to_bounding_box(image_tensor, 0, 0, crop_height, crop_width)

    # Resize the cropped tensor
    resized_tensor = tf.image.resize(croped_tensor, [target_height, target_width])

    return resized_tensor

# Example usage
input_image = tf.random.uniform((224, 224, 3), name='input_image')  # Example input image tensor
cropped_resized_image = crop_and_resize(input_image, 128, 128, 256, 256)

print(cropped_resized_image)
