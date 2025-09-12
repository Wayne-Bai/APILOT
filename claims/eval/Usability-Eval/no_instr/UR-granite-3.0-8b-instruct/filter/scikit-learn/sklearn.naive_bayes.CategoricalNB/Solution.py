from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import make_pipeline

# Assuming X is your categorical features and y is your target variable
# X = [['cat', 'dog'], ['bird', 'fish'], ['cat', 'fish']]
# y = ['mammals', 'fish', 'mammals']

# Create a pipeline that first converts categorical features to a matrix of token counts,
# and then applies the Naive Bayes classifier.
model = make_pipeline(CountVectorizer(), MultinomialNB())

# Train the model using your data
model.fit(X, y)

# Now you can use the model to predict the target variable for new data
predictions = model.predict([['cat', 'bird']])
print(predictions)
