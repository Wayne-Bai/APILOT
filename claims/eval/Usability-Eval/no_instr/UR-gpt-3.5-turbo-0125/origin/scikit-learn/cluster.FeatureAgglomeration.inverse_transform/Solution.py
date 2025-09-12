
import numpy as np

def inverse_transformation(transformation_matrix, transformed_vector):
    return np.linalg.pinv(transformation_matrix).dot(transformed_vector)
