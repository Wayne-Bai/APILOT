from sklearn.cluster import SpectralClustering
from sklearn import datasets

# Load Data
# data = datasets.load_iris().data
# For the purpose of demonstration, I'll use iris data which is a 150x4 numpy array
# If your data is in a different format, you might need to prepare it appropriately
data = datasets.load_iris().data

# Define the SpectralClustering function
sc = SpectralClustering(n_clusters=2, affinity='nearest_neighbors')

# Fit the data into the model
labels = sc.fit_predict(data)

print(labels)
