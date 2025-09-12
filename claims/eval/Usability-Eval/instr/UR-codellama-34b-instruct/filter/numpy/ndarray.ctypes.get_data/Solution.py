import numpy as np

# Create a NumPy array with some random data
arr = np.random.randint(0, 100, size=(5,))

# Access the memory area of the array using the .data attribute
buf = arr.data

# Use the memoryview module to access and manipulate the data in the buffer
with buf.memoryview() as view:
    # Manipulate the data in the buffer
    print(f"Before manipulation: {arr}")
    for i, x in enumerate(buf):
        view[i] = x * 2
    print(f"After manipulation: {arr}")
