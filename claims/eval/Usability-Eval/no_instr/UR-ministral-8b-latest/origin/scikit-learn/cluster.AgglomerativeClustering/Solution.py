from sklearn.cluster import AgglomerativeClustering
import numpy as np

# Sample data
X = np.random.rand(100, 10)

# Initializing the model
model = AgglomerativeClustering(n_clusters=3, affinity='euclidean', linkage='ward')

# Fitting the model
clusters = model.fit_predict(X)

print(clusters)
