import tensorflow as tf

class BaseExtensionType(tf.experimental.ExtensionType):
    def __init__(self):
        super().__init__()

    def some_method(self):
        # Implement your custom behavior here
        pass

# Example subclass that extends BaseExtensionType
class MyCustomType(BaseExtensionType):
    def __init__(self, value):
        super().__init__()
        self.value = value

    def some_method(self):
        # Custom implementation for MyCustomType
        return self.value + 1
