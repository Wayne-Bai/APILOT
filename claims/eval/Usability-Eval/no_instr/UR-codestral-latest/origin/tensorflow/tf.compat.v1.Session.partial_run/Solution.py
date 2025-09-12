import tensorflow as tf

# Placeholder for input data
input_data = tf.placeholder(tf.float32)

# Operation to compute (just an example, you can replace it with your actual operations)
result = tf.square(input_data)

# Start a new TensorFlow session
with tf.Session() as sess:
    for i in range(10):
        # Feed the input data with a value
        feed_dict = {input_data: float(i)}

        # Run the operation and fetch the result
        output = sess.run(result, feed_dict=feed_dict)
        print(f"The square of {i} is {output}")
