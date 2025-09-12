from sklearn.cross_decomposition import CCA

# define the CCA model with 1 component
model = CCA(n_components=1)

# fit the model on the training data
# model.fit(X_train, Y_train)

# transform the test data
# X_test_transformed = model.transform(X_test)
# Y_test_transformed = model.transform(Y_test)
