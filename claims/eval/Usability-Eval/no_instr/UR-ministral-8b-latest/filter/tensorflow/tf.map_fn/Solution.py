import tensorflow as tf

def transform_data(data, fn):
    return fn(tf.unstack(data, axis=0))

# Example usage:
data = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=tf.int32)
def add_one(x):
    return x + 1

transformed_data = transform_data(data, add_one)
print(transformed_data)
