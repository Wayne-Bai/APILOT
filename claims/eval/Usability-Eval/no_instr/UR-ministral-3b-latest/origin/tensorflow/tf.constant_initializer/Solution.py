import tensorflow as tf

# Define the custom initializer
def constant_initializer(const_value):
    class ConstantInitializer(tf.keras.initializers.Initializer):
        def __call__(self, shape, dtype=None, **kwargs):
            return tf.constant(const_value, dtype=dtype, shape=shape)

        def get_config(self):
            return {'value': const_value}

        @property
        def value(self):
            return const_value

# Example usage
initial_value = 42
custom_initializer = constant_initializer(initial_value)

# Create a variable with the custom initializer
var = tf.Variable(tf.random.normal(shape=(2, 2)))
var.assign(tf.reduce_sum(var) + initial_value)

print("Var's shape:", var.shape)  # Output: Var's shape: [12]
