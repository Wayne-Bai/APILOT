import nltk
from nltk.tokenize.punkt import PunktSentenceTokenizer

text = """Your text goes here. Replace this with any text in which you want to find sentence boundaries.
This can include multiple sentences, paragraphs, or even large documents."""

# Train the tokenizer
tokenizer = PunktSentenceTokenizer()
tokenizer.train(text)

# Tokenize the text
sentences = tokenizer.tokenize(text)

print(sentences)
