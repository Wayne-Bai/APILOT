import tensorflow as tf

def resize_image(image, target_height, target_width):
    # Start the _BeforeResize operations
    resized = tf.raw_ops.Resize(
        image=image,
        target_height=target_height,
        target_width=target_width,
        resize_method='BILINEAR'
    )
    # End the _Resize operations

    return resized
