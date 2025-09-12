from sklearn.decomposition import DictionaryLearning

def fit_dictionary(data, n_components):
    # Initialize the DictionaryLearning object
    dictionary = DictionaryLearning(n_components=n_components)

    # Fit the dictionary to the data
    dictionary.fit(data)

    return dictionary
