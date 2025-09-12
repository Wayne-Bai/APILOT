import tensorflow as tf

# Create some random data
data = tf.random.normal([2, 5, 5, 5])
print("Data:", data)

# Define the maxpooling filter
filter_shape = [2, 2]
kernel = tf.constant(1.0, shape=filter_shape)

# Define the maxpooling operator
def maxpooling(pool, filter_shape, stride):
    pooled = tf.nn.max_pool(pool,
                           ksize=[1, stride, stride, 1],
                           strides=[1, stride, stride, 1],
                           padding='VALID')
    return pooled

# Define the maxpooling gradient operator
def maxpool_grad_wrt_weight(input_, filter_shape, w_):
    input_, w_ = tf.convert_to_tensor(input_), tf.convert_to_tensor(w_)
    pool = input_[:, -filter_shape[0]:, -filter_shape[1]:, :]
    grad = tf.logical_and(pool >= (0.5 * w_),
                          tf.logical_not(tf.equal(pool, 0.0)))
    grad = tf.reduce_sum(grad, axis=[1, 2]) / tf.reduce_sum(grad_shape, axis=1) / stride
    return grad

# Define the gradient function
def maxpooling_gradient(inputs, filter_shape, w_):
    gradient = maxpool_grad_wrt_weight(inputs, filter_shape, w_)
    return gradient

# Compute the input to the gradient function
inputs = tf.raw_ops.Conv2D()(data, filters=w_, kernel_size=filter_shape)

# Compute the gradient
gradient = maxpooling_gradient(inputs, filter_shape, w_)
print("Gradient:", gradient)
