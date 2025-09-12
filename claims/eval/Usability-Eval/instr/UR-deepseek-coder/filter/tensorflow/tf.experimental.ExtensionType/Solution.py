import tensorflow as tf

class MyExtensionType(tf.experimental.ExtensionType):
    value: tf.Tensor

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"MyExtensionType(value={self.value})"

# Example usage
tensor = tf.constant([1, 2, 3])
ext_type_instance = MyExtensionType(tensor)
print(ext_type_instance)
