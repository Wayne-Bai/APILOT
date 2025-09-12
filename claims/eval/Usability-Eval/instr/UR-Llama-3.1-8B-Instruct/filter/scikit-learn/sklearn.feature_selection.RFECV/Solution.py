# Import necessary libraries from scikit-learn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import RFECV
from sklearn.model_selection import StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV

# Load the iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split the dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Initialize a StandardScaler object
scaler = StandardScaler()

# Fit the scaler to the training data and transform both the training and test data
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Initialize a Logistic Regression model
model = LogisticRegression()

# Initialize an RFECV object with 5 folds of cross-validation
selector = RFECV(estimator=model, step=1, cv=StratifiedKFold(5), scoring='accuracy')

# Fit the selector to the training data
selector.fit(X_train_scaled, y_train)

# Print the selected features
print("Selected features:", selector.support_)
print("Feature ranking:", selector.ranking_)
print("Optimal number of features:", selector.n_features_)

# Transform the training and test data using the selected features
X_train_trans = selector.transform(X_train_scaled)
X_test_trans = selector.transform(X_test_scaled)

# Now, you can use the transformed data for further analysis or modeling
