import tensorflow as tf

class MyBaseExtensionType(tf.Module):
    def __init__(self, name=None):
        super(MyBaseExtensionType, self).__init__(name=name)
        # Initialize any properties that are common across your custom types

    def my_custom_method(self):
        # Define any common behavior for your extension types here
        pass

# Example subclass using MyBaseExtensionType
class CustomType(MyBaseExtensionType):
    def __init__(self, data):
        super(CustomType, self).__init__()
        self.data = tf.Variable(data)

    def my_custom_method(self):
        return tf.reduce_sum(self.data)

# Using the CustomType
ct = CustomType([1, 2, 3])
print(ct.my_custom_method())
