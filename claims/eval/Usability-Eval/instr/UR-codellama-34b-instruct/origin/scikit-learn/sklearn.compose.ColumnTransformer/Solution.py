import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline

# create a dataset with 4 columns: 2 numeric and 2 categorical
X = np.array([[1, 'a', 3, 'c'], [2, 'b', 4, 'd']])
y = np.array([0, 1])

# define the column transformers
numeric_transformer = StandardScaler()
categorical_transformer = OneHotEncoder(sparse=False)

# create a pipeline with the column transformers and the logistic regression model
pipe = make_pipeline(ColumnTransformer([('numeric', numeric_transformer, [0, 2]),
                                        ('categorical', categorical_transformer, [1, 3])]),
                     LogisticRegression())

# fit the pipeline to the data
pipe.fit(X, y)

# make predictions on new data
new_data = np.array([[10, 'a'], [20, 'b']])
preds = pipe.predict(new_data)
print(preds)
