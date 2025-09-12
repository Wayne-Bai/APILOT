from sklearn import svm
from sklearn.datasets import make_classification

# Create a random n-class classification problem
X, y = make_classification(n_samples=100, n_features=2, n_informative=2, n_redundant=0, n_clusters_per_class=1, random_state=42)

# Create a SVM classifier
clf = svm.SVC(kernel='linear')

# Train the classifier
clf.fit(X, y)
