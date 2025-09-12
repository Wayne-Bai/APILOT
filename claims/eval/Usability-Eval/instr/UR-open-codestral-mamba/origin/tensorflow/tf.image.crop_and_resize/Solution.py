import tensorflow as tf

def crop_and_resize(input_tensor, boxes, crop_size):
    # Prepare the output tensor with the given number of crops based on the number of boxes
    outputs = tf.zeros([boxes.shape[0], crop_size[0], crop_size[1], input_tensor.shape[3]])

    # For each bounding box
    for i in range(boxes.shape[0]):
        # Extract the crop from the input tensor using the bounding box indices
        crop = tf.image.crop_and_resize(input_tensor, [boxes[i]], [0], crop_size)

        # Resize the crop using the bicubic interpolation method
        crop = tf.image.resize(crop, [crop_size[0], crop_size[1]], method='bicubic')

        # Add the crop to the output tensor
        outputs[i] = crop[0]

    return outputs
