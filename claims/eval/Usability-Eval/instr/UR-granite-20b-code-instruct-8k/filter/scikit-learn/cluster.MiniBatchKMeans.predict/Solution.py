from sklearn.cluster import KMeans

# Assuming you have the data in a variable named X

kmeans = KMeans(n_clusters=3, random_state=0).fit(X)
predictions = kmeans.predict(X)
