import tensorflow as tf

class BaseExtensionType(tf.experimental.extension.ExtensionType):
    """Base class for TensorFlow ExtensionType classes."""

    def __init__(self, value):
        self.value = value

    @property
    def dtype(self):
        raise NotImplementedError("Subclasses must implement this property.")

    def __repr__(self):
        return f"{self.__class__.__name__}(value={self.value})"

# Example subclass implementation
class CustomType(BaseExtensionType):
    """Example subclass of BaseExtensionType."""

    @property
    def dtype(self):
        return tf.float32  # Example dtype

# Example usage
custom_instance = CustomType(value=42.0)
print(custom_instance)
print("Dtype:", custom_instance.dtype)
