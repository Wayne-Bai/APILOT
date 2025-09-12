import tensorflow as tf
from typing import Any, List

# Define a base class for TensorFlow ExtensionTypes
class MyExtensionType(tf.experimental.ExtensionType):
    # Define the parameters and their types
    field1: tf.Tensor
    field2: List[int]
    field3: float
    
    def __init__(self, field1: tf.Tensor, field2: List[int], field3: float):
        # Initialize fields
        self.field1 = field1
        self.field2 = field2
        self.field3 = field3

    def get_fields(self) -> Any:
        # A sample method to retrieve all fields
        return self.field1.numpy(), self.field2, self.field3

# Example usage
field1_example = tf.constant([1.0, 2.0, 3.0], dtype=tf.float32)
field2_example = [1, 2, 3]
field3_example = 3.14

extension_instance = MyExtensionType(field1_example, field2_example, field3_example)
print("Fields:", extension_instance.get_fields())
