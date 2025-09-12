import numpy as np

def compute_qth_percentile(data, q, axis=None):
    if axis is None:
        return np.percentile(data, q, interpolation='linear')
    else:
        return np.percentile(data, q, axis=axis, interpolation='linear')

# Example usage:
data = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
q = 50
result = compute_qth_percentile(data, q)
print(f"The {q}th percentile of the data is: {result}")

data_2d = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
q_axis = 0
result_axis = compute_qth_percentile(data_2d, q_axis)
print(f"The {q_axis}th percentile along axis 0 is: {result_axis}")
