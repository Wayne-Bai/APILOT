
# Importing the necessary libraries
from sklearn.cluster import KMeans

# Creating an instance of KMeans
kmeans = KMeans(n_clusters=3, random_state=0)

# Fitting the KMeans model to the data
kmeans.fit(X)

# Predicting the closest cluster each sample in X belongs to
closest_clusters = kmeans.predict(X)
