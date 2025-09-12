from nltk.corpus import wordnet

def calculate_information_content(synset):
    synset = wordnet.synsets(synset)
    if not synset:
        return 0

    words = [word.lemmas()[0].name() for synset in synset for word in synset.lemmas()]
    word_freq = {word: words.count(word) for word in set(words)}

    info_content = sum(freq / len(words) for freq in word_freq.values())
    return info_content

# Example usage:
synset = "nuclear"
print(calculate_information_content(synset))
