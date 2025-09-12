import tensorflow as tf

class MyScope(tf.VariableScope):
    def __init__(self, name):
        super(MyScope, self).__init__(name)

    def variables(self, *args, **kwargs):
        with self:
            return super(MyScope, self).variables(*args, **kwargs)

# Usage
with MyScope('my_scope'):
    v1 = tf.Variable(1.0, name='v1')
    v2 = tf.Variable(2.0, name='v2')

# Print the variables
print(v1)
print(v2)
