import tensorflow as tf

class MyObject(tf.Module):
    def __init__(self, value):
        super(MyObject, self).__init__()
        self.value = tf.Variable(value)

    @tf.function
    def multiply(self, x):
        return self.value * x

# Example usage
obj = MyObject(value=5)
result = obj.multiply(10)
print(result.numpy())
