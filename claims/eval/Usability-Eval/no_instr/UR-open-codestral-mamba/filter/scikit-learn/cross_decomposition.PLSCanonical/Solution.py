
import sklearn
from sklearn.cross_decomposition import PLSRegression

# create a PLSRegression instance
pls2 = PLSRegression(n_components=2)

# suppose X_train and Y_train are your training datasets
X_train = [[0., 0.], [1., 1.], [2., 2.]]
Y_train = [0.1, 0.2, 0.3]

# fit the model with data (Training the model)
pls2.fit(X_train, Y_train)

# suppose X_test and Y_test are your testing datasets
X_test = [[0., 0.], [1., 1.], [2., 2.]]

# Predicting for testing dataset
Y_predicted = pls2.predict(X_test)

print('Predicted values for testing dataset: ', Y_predicted)
