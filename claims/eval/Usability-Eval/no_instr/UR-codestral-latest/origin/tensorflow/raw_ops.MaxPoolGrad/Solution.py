import tensorflow as tf

# Creating a tensor for input
x = tf.constant([[[1., 1., 2.],
                  [2., 2., 1.],
                  [3., 3., 3.]],
                 [[4., 4., 5.],
                  [5., 5., 6.],
                  [6., 6., 7.]]], dtype=tf.float32)
x = tf.reshape(x, [1, 2, 3, 3])

# Creating a tensor for gradient
dy = tf.constant([[[[1., 1.],
                   [1., 1.],
                   [1., 1.]],
                  [[1., 1.],
                   [1., 1.],
                   [1., 1.]]]], dtype=tf.float32)

# We don't need to define a model for this, just use tf.nn.max_pool to get the output and gradients
pooled = tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 1, 1, 1], padding='VALID')
gradients = tf.gradients(ys=[pooled], xs=[x], grad_ys=[dy])[0]

# Running the Tensorflow session
with tf.Session() as sess:
  pooled_result, gradients_result = sess.run([pooled, gradients])
  print("Pooled result:\n", pooled_result)
  print("Gradients:\n", gradients_result)
