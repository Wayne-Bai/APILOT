from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB

# Load iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Split the dataset into a training set and a testing set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features to have mean=0 and variance=1
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Initialize Gaussian Naive Bayes
gnb = GaussianNB()

# Fit the model
gnb.partial_fit(X_train, y_train, classes=np.unique(y))

# Predict
y_pred = gnb.predict(X_test)
