import tensorflow as tf

def my_func(x):
 return x * x

graph_func = tf.function(my_func)
