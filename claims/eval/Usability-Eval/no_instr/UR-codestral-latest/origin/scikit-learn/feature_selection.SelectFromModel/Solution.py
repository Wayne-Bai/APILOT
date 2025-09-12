from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectFromModel
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

# Loading some data
iris = load_iris()
X = iris.data
y = iris.target

# Splitting data into training and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 123)

# Creating a RandomForest model
model = RandomForestClassifier(n_estimators=100)

# Training the model on training data
model.fit(X_train, y_train)

# Creating a selector object that will keep features which importance is greater than a threshold
selector = SelectFromModel(model, threshold='mean')

# Transforming the training and test data
X_train_transformed = selector.fit_transform(X_train, y_train)
X_test_transformed = selector.transform(X_test)

# Printing the shape of the transformed data
print("Shape of the transformed training data: ", X_train_transformed.shape)
print("Shape of the transformed test data: ", X_test_transformed.shape)
