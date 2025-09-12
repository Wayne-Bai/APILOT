import numpy as np
import tensorflow as tf

# Function to convert a numpy array to DLTensor
def numpy_to_dlpack(capsule):
    # Ensure the input is a numpy array
    if not isinstance(capsule, np.ndarray):
        raise ValueError("Input should be a numpy array")

    # Convert numpy array to tensor
    tensor = tf.constant(capsule)

    # Get DLTensor capsule
    dl_tensor = tensor._dlpack

    return dl_tensor

# Example usage
if __name__ == "__main__":
    numpy_array = np.array([[1.0, 2.0], [3.0, 4.0]])
    dlpack_capsule = numpy_to_dlpack(numpy_array)

    print("DLTensor Capsule:", dlpack_capsule)
