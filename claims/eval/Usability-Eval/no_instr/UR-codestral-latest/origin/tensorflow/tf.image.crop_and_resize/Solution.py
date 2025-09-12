import tensorflow as tf

def crop_and_resize(image_tensor, crop_box, new_size):
    # Crop the image
    cropped_images = tf.image.crop_and_resize(image_tensor, crop_box, box_ind=None, crop_size=new_size)

    return cropped_images

# Example usage:
image_tensor = tf.random.normal([1, 100, 100, 3])  # Replace with your image tensor
crop_box = tf.constant([[0.1, 0.1, 0.9, 0.9]])  # A single crop box in [ymin, xmin, ymax, xmax] format (normalized)
new_size = [50, 50]  # Desired size

cropped_images = crop_and_resize(image_tensor, crop_box, new_size)
