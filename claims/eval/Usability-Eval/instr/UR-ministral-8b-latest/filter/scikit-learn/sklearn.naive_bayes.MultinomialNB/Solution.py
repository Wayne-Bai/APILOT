import numpy as np
import pandas as pd
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

# Load the 20 newsgroups dataset
data = fetch_20newsgroups(subset='train')

# Create a pipeline with CountVectorizer and MultinomialNB
model = make_pipeline(CountVectorizer(), MultinomialNB())

# Train the model
model.fit(data.data, data.target)

# Predict the category of a sample document
sample_document = ["We need to clean the house tomorrow", "Python is a general-purpose language."]
predictions = model.predict(sample_document)

# Print the predictions
for i, prediction in enumerate(predictions):
    print(f"Document {i+1} is predicted to belong to class '{data.target_names[prediction]}'")
