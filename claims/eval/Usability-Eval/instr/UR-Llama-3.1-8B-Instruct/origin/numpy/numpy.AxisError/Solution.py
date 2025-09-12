import numpy as np

try:
    # Create a 2D array
    array_2d = np.array([[1, 2, 3], [4, 5, 6]])

    # Incorrect axis specified
    np.sum(array_2d, axis=2)

except ValueError as ve:
    print("A ValueError occurred: ", ve)
except IndexError as ie:
    print("An IndexError occurred: ", ie)
except np.AxisError as ae:
    print("A numpy.AxisError occurred: ", ae)
