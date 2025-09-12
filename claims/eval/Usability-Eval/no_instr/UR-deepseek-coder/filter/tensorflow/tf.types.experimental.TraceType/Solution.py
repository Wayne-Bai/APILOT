import tensorflow as tf

class ObjectType:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"ObjectType(name={self.name})"

# Example usage
obj = ObjectType("example_object")

@tf.function
def process_object(obj):
    print(f"Processing object: {obj}")
    return obj.name

# Trace the function with the object
result = process_object(obj)
print(f"Result: {result}")
