import tensorflow as tf

class MyObject:
    def __init__(self, value):
        self.value = value

    @tf.function
    def square(self):
        return tf.square(self.value)

# Create an instance of MyObject
obj = MyObject(tf.constant(5))

# Call the square method
result = obj.square()

print(result)
