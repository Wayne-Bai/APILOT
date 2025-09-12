import tensorflow as tf

def crop_and_resize_image(image_tensor, crop_size):
    # Crop the image tensor
    cropped_image = tf.image.crop_to_bounding_box(image_tensor,
                                                 offset_height=0,
                                                 offset_width=0,
                                                 target_height=crop_size,
                                                 target_width=crop_size)

    # Resize the cropped image tensor
    resized_image = tf.image.resize(cropped_image, [crop_size, crop_size])

    return resized_image

# Example usage
input_image = tf.constant([[[1, 0, 0], [0, 1, 0], [0, 0, 1]]], dtype=tf.float32)  # Replace this with your image tensor
crop_size = 3  # Desired crop size
output_image = crop_and_resize_image(input_image, crop_size)
print(output_image)
