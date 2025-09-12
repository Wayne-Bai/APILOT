import tensorflow as tf

class MyTensorFlowExtensionType(tf.experimental.ExtensionType):
    # Define the fields of the ExtensionType
    field1: tf.Tensor
    field2: tf.Tensor

    def my_method(self):
        # You can define methods that operate on the fields
        return self.field1 + self.field2

# Example usage
obj = MyTensorFlowExtensionType(
    field1=tf.constant([1, 2, 3]),
    field2=tf.constant([4, 5, 6])
)
result = obj.my_method()
print(result)
