
# Importing the necessary library
from sklearn.cluster import KMeans

# Creating an instance of KMeans clustering model
kmeans = KMeans(n_clusters=3)

# Fitting the model with the data X
kmeans.fit(X)

# Predicting the closest cluster for each sample in X
labels = kmeans.predict(X)
