import numpy as np
import pandas as pd
from sklearn.cross_validation import KFold
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
from sklearn.cross_validation import predict
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

X_train = np.random.rand(100, 5)
y_train = np.random.randint(0, 2, size=(100, 1))

# Pipeline
pipe = make_pipeline(StandardScaler())

kf = KFold(y_train.size)
error = []

for train_index, test_index in kf.split(X_train):
    X_train_fold, X_test_fold = X_train[train_index], X_train[test_index]
    y_train_fold, y_test_fold = y_train[train_index], y_train[test_index]

    pipeline = make_pipeline(
        StandardScaler(),
        PCA(n_components=2)
    )

    X_train_fold = pipeline.fit_transform(X_train_fold)
    X_test_fold = pipeline.transform(X_test_fold)

    dtr = GaussianNB()
    dtr.fit(X_train_fold, y_train_fold)
    prediction = dtr.predict(X_test_fold)

    diff = y_test_fold - prediction
    error.append(diff)

error = np.mean(np.square(error))
print(f"Mean squared prediction error for scoring model: {error:.2f}")

