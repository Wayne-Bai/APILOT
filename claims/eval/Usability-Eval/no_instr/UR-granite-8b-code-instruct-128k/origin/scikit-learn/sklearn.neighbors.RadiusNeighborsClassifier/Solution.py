from sklearn.neighbors import KNeighborsClassifier

# Create a KNeighborsClassifier object with n_neighbors=5 and radius=0.5
knn = KNeighborsClassifier(n_neighbors=5, radius=0.5)

# Fit the classifier to the training data
knn.fit(X_train, y_train)

# Predict the labels for the test data
y_pred = knn.predict(X_test)
