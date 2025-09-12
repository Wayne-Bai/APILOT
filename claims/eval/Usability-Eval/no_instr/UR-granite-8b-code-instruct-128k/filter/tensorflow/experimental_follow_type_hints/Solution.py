import tensorflow as tf

def my_function(x: tf.Tensor, y: tf.Tensor) -> tf.Tensor:
    return x + y

@tf.function(jit_compile=True)
def my_compiled_function(x: tf.Tensor, y: tf.Tensor) -> tf.Tensor:
    return my_function(x, y)

x = tf.constant(1)
y = tf.constant(2)

result = my_compiled_function(x, y)
print(result)  # Output: 3
