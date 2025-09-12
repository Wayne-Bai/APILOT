from sklearn.cross_decomposition import PLSRegression

X = [[0, 0, 1], [1, 0, 0], [2, 2, 2], [3, 5, 4]]
y = [0, 1, 2, 3]

pls = PLSRegression(n_components=2)
pls.fit(X, y)

X_pred = [[1, 1, 1], [2, 2, 2]]
y_pred = pls.predict(X_pred)
