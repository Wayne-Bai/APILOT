import tensorflow as tf

def serialize_protobuf(model):
    # Assuming 'model' is a TensorFlow model or a protobuf object
    serialized_model = model.SerializeToString()
    return serialized_model

# Example usage:
# Assuming 'model' is a TensorFlow model or a protobuf object
# serialized_model = serialize_protobuf(model)
# print(serialized_model)
