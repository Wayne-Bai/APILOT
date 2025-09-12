from sklearn.decomposition import TruncatedSVD
from sklearn.cross_decomposition import PLSRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

# Load the iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Create a pipeline with SVD and PLSRegression
pls = make_pipeline(TruncatedSVD(n_components=2), PLSRegression(n_components=2))

# Fit the pipeline to the training data
pls.fit(X_train, y_train)

# Make predictions on the test data
y_pred = pls.predict(X_test)

# Print the predictions
print(y_pred)
