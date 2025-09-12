from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

def create_complement_nb_classifier():
    model = make_pipeline(
        CountVectorizer(),
        MultinomialNB()
    )
    return model

# Replace this with your data
texts = ["I love programming", "This is a great book", "Sklearn is amazing", "I hate bugs"]
labels = ["positive", "positive", "positive", "negative"]

complement_nb = create_complement_nb_classifier()
complement_nb.fit(texts, labels)
