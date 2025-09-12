from sklearn.neighbors import RadiusNeighborsClassifier
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

# Load Iris dataset as an example
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize feature values for better performance
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Create a Radius Neighbors Classifier with a radius of 1
# and 2 neighbors to include in the voting process
classifier = make_pipeline(StandardScaler(),
                           RadiusNeighborsClassifier(radius=1, n_neighbors=2))

# Fit the classifier to the training data
classifier.fit(X_train_scaled, y_train)

# Predict the labels of the test set
y_pred = classifier.predict(X_test_scaled)

# To check the classifier's performance, print the first 10 predictions
print(y_pred[:10])
