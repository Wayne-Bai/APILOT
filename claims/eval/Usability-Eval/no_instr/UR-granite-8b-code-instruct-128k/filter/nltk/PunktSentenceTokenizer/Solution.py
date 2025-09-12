import nltk
from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktTrainer
from nltk.tokenize import word_tokenize

sentences = [
    "This is a sentence.",
    "This is another sentence.",
    "And this is yet another sentence.",
]

# Tokenize the sentences
tokenizer = PunktSentenceTokenizer()
tokenizer.train(sentences)

# Test the tokenizer on some sample text
text = "This is a sentence. This is another sentence. And this is yet another sentence."
tokens = tokenizer.tokenize(text)

print(tokens)
