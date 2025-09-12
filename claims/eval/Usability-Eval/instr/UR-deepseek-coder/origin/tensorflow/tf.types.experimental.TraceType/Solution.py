import tensorflow as tf

class ObjectType:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"ObjectType(name={self.name})"

# Example usage
obj = ObjectType("example_object")

# This function will be traced by tf.function
@tf.function
def process_object(obj):
    print(f"Processing object: {obj}")
    return obj.name

# Call the function
result = process_object(obj)
print(f"Result: {result}")
