import scipy.spatial.transform as sptf

# Example data and transform matrices can be provided here
# data: your data points
# transform: your initial transform matrix

# Convert the data to quaternions if necessary
transform = sptf.Quat()

transform.from_matrix(data)

transform.to_matrix(quaternions)
