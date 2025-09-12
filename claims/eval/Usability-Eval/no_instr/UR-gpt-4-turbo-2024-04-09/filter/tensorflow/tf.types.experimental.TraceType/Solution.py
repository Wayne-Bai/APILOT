import tensorflow as tf

@tf.function(input_signature=[tf.TensorSpec(shape=[None], dtype=tf.float32)])
def my_function(x):
    return x * 2

# Tracing the function
result = my_function(tf.constant([1.0, 2.0, 3.0]))
print(result)
