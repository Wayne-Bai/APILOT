from sklearn.feature_extraction.text import CountVectorizer

def compute_sparse_vector_density(text_corpus, num_features):
    # Vectorize the text corpus using CountVectorizer
    vectorizer = CountVectorizer(max_features=num_features)
    X = vectorizer.fit_transform(text_corpus)

    # Compute density of the sparse vector
    densities = (X.toarray() > 0).mean(axis=0)

    return densities

# Example usage
text_corpus = [
    "This is the first document.",
    "This document is the second document.",
    "And this is the third one.",
    "Is this the first document?"
]

num_features = 5
density = compute_sparse_vector_density(text_corpus, num_features)
print(density)
