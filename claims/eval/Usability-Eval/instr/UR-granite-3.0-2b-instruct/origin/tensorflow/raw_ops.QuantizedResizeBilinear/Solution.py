import tensorflow as tf

def resize_quantized_images(images, target_size):
    # Create a resize operation with quantized bilinear interpolation
    resize_op = tf.raw_ops.ResizeBilinearQuantized(
        images=images,
        target_size=[target_size, target_size],
        align_corners=True,
        half_pixel_centers=True
    )

    # Run the operation to get the resized images
    resized_images = resize_op.execute()

    return resized_images
