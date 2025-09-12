# importing the necessary libraries
from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# load pre-trained dataset
iris = datasets.load_iris()
# get the data and target
X = iris.data
y = iris.target

# standardize the data
sc = StandardScaler()
X = sc.fit_transform(X)

# compute the kernel in a low-dimensional space
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# apply k-means clustering
kmeans = KMeans(n_clusters=3, random_state=0)
clusters = kmeans.fit_predict(X_pca)

# print the first 5 clustered labels
print(clusters[:5])
