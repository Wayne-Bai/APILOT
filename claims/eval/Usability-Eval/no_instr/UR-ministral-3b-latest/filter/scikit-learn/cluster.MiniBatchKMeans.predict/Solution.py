from sklearn.cluster import KMeans

# Assuming X is your input data and n_clusters is the number of clusters
n_clusters = 3
cluster_labels = KMeans(n_clusters=n_clusters).fit_predict(X)
