from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import label_binarize
from sklearn.isotonic import IsotonicRegression
import numpy as np

# Assume we have some binary classification model that outputs probabilities
y_true = np.array([0, 0, 1, 1])
y_pred_uncalib = np.array([0.1, 0.4, 0.35, 0.8])

# Calibrate the probabilities using isotonic regression
y_true_binary = label_binarize(y_true, classes=[0, 1])
clf = IsotonicRegression()
clf.fit(y_pred_uncalib, y_true_binary[:, 1])
y_pred_calib = clf.predict(y_pred_uncalib)

# Now y_pred_calib are calibrated probabilities
print(y_pred_calib)
