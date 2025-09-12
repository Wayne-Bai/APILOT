import tensorflow as tf

@tf.function(experimental_compile=True)
def my_model(x):
    # A simple example model
    return tf.reduce_sum(tf.matmul(x, x), axis=1)

# Example usage
input_data = tf.random.normal([128, 128])
result = my_model(input_data)
print(result)
