from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import LabelEncoder

# Assuming you have your data in X (feature matrix) and y (target array)
X = ...
y = ...

# Encoding categorical features
le = LabelEncoder()
X_encoded = le.fit_transform(X)

# Creating pipeline
clf = make_pipeline(DecisionTreeClassifier(random_state=42))

# Fitting the model
clf.fit(X_encoded, y)

# Making predictions
X_new = ...
y_pred = clf.predict(X_new)
