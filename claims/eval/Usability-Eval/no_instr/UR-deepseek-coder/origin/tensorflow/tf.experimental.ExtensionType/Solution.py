import tensorflow as tf

class TensorFlowExtensionType(tf.experimental.ExtensionType):
    """Base class for TensorFlow ExtensionType classes."""

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"{self.__class__.__name__}(value={self.value})"

    def __eq__(self, other):
        if isinstance(other, TensorFlowExtensionType):
            return self.value == other.value
        return False

# Example usage
class MyTensorType(TensorFlowExtensionType):
    def __init__(self, value, additional_info):
        super().__init__(value)
        self.additional_info = additional_info

    def __repr__(self):
        return f"{self.__class__.__name__}(value={self.value}, additional_info={self.additional_info})"

# Creating an instance of MyTensorType
my_tensor = MyTensorType(value=tf.constant([1, 2, 3]), additional_info="example info")
print(my_tensor)
