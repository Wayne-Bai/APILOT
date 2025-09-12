import tensorflow as tf

class ResizeQuantizedImage:
    def __call__(self, input_image, target_size):
        # Ensure the input_image is quantized
        input_image = tf.math.quantize_per_channel(input_image, [16], tf.qint32)

        # Pad the input_image to enable resizing
        padded_image = self.pad_image(input_image, target_size)

        # Resize the padded image
        resized_image = self.resize_image(padded_image, target_size)

        return resized_image

    def pad_image(self, input_image, target_size):
        input_shape = tf.shape(input_image)
        pad_amount = tf.math.ceil(tf.cast(target_size // 2, tf.float32))

        x_padding = (pad_amount, pad_amount)
        y_padding = (pad_amount, pad_amount)

        padded_image = tf.pad(input_image, [[0, 0], x_padding, y_padding], mode='CONSTANT')
        return padded_image

    def resize_image(self, input_image, target_size):
        # Perform Resize using bilinear interpolation
        tf.raw_ops.Resize(
            input=input_image,
            size=target_size,
            method='bilinear'
        )
