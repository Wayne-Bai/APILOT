import tensorflow as tf

def extract_and_resize_images(input_tensor, boxes, box_indices, crop_size):
    """
    Extracts crops from the input image tensor and resizes them using the provided boxes.

    Args:
    - input_tensor (tf.Tensor): The input tensor image of shape (batch_size, height, width, channels).
    - boxes (tf.Tensor): A 2-D tensor of shape `[num_boxes, 4]`. Each row of the tensor specifies
      the coordinates of a box in normalized coordinates `[y1, x1, y2, x2]`.
    - box_indices (tf.Tensor): A 1-D tensor of type int32 / int64, containing indices of the images
      in the batch to which each box corresponds.
    - crop_size (list or tuple of two ints): The size to resize the cropped image to.

    Returns:
    - tf.Tensor: A 4-D tensor containing the cropped and resized images of shape
      `[num_boxes, crop_height, crop_width, channels]`.
    """
    cropped_images = tf.image.crop_and_resize(
        input_tensor, boxes, box_indices, crop_size)
    return cropped_images

# Example usage:
if __name__ == "__main__":
    # Input image tensor of shape (batch_size, height, width, channels)
    input_images = tf.random.normal([5, 300, 300, 3])  # Example tensor

    # Define the boxes - normalized coordinates (y1, x1, y2, x2)
    boxes = tf.constant([
        [0.1, 0.1, 0.5, 0.5],  # Box 1
        [0.5, 0.5, 1.0, 1.0]   # Box 2
    ], dtype=tf.float32)

    # Indices of input images to apply boxes
    box_indices = tf.constant([0, 1], dtype=tf.int32)

    # Size of the crop
    crop_size = [100, 100]

    # Extract and resize
    output_images = extract_and_resize_images(input_images, boxes, box_indices, crop_size)
    print("Cropped and resized images tensor shape:", output_images.shape)
