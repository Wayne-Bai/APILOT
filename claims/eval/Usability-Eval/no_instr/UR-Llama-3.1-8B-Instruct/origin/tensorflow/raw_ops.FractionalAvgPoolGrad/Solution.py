# Import necessary libraries from tensorflow
import tensorflow as tf

# Define the input tensors
x = tf.random.normal([1, 3, 3, 6])  # Input tensor of shape (batch_size, height, width, channels)

# Define the FractionalAvgPool function
class FractionalAvgPool(tf.Module):
    def __init__(self, pooling_size, sampling_ratio, name=None):
        super(FractionalAvgPool, self).__init__(name=name)
        self.pooling_size = pooling_size
        self.sampling_ratio = sampling_ratio

    @tf.function
    def __call__(self, x):
        with tf.name_scope(self.name or 'FractionalAvgPool'):
            # Calculate the ds_tensor
            height_ds_tensor = tf.cast(1.0 / self.pooling_size[0], tf.float32)
            width_ds_tensor = tf.cast(1.0 / self.pooling_size[1], tf.float32)

            # Calculate the ds_args
            ds_args = {}
            ds_args['height'] = tf.cast(1.0 / self.polling_size[0], tf.float32)
            ds_args['width'] = tf.cast(1.0 / self.pooling_size[1], tf.float32)

            ds_args['sampling_ratio'] = self.sampling_ratio

            # Compute the FractionalAvgPool
            factional_avgpool_output = tf.raw_ops.FractionalAvgPool(
                input=x,
                pool_tensor=tf.constant([[[[3.0, 3.0], [1.0, 5.0]]]]),
                sampling_ratio=[.5,.5, 1, 0],
            )

            # Compute the gradient
            g_mu = tf.gradients(factional_avgpool_output, x)

            return g_mu, factional_avgpool_output


# Create an instance of FractionalAvgPool
fractional_avg_pool = FractionalAvgPool(pooling_size=[2, 2], sampling_ratio=.5)

# Get the gradient
g_mu, kb_fractional_avgpool_out = fractional_avg_pool(x)

# Print the result
print(kb_fractional_avgpool_out)
