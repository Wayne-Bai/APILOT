
import tensorflow as tf

def apply_layout(scope, layout):
    var_list = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES, scope=scope)
    for var in var_list:
        for key, value in layout.items():
            if key in var.name:
                var.assign(value)


# Example usage
layout = {
    'weight': tf.random.normal(shape=(3, 3)),
    'bias': tf.zeros(shape=(3,))
}

with tf.variable_scope('model'):
    var1 = tf.Variable(tf.zeros(shape=(3, 3)), name='weight')
    var2 = tf.Variable(tf.ones(shape=(3,)), name='bias')

apply_layout('model', layout)
