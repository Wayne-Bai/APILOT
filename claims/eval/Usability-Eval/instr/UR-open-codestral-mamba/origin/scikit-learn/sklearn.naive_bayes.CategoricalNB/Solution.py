from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.naive_bayes import CategoricalNB
from sklearn.pipeline import make_pipeline

# Assuming that X is your data and y is the target variable
X, y = None, None # replace None with your dataset

# Let's assume that categorical_features is list of indices or column names of categorical columns.
# Here, we assume that it is ['feature1', 'feature2'].
categorical_features = ['feature1', 'feature2']

# OneHotEncode the categorical columns
preprocessor = ColumnTransformer(transformers=[('categorical', OneHotEncoder(), categorical_features)])

# Categorical Naive Bayes Classifier
clf = make_pipeline(preprocessor, CategoricalNB())

# Now, we can fit our classifier
clf.fit(X, y)

# And do predictions
predictions = clf.predict(new_data)
