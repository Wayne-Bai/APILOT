import nltk
from nltk.tokenize.punkt import PunktSentenceTokenizer

# Sample text
text = """This is a sample text. Dr. Smith is coming at 8:00 pm. Isn't that great? I hope it doesn't rain tomorrow. London, being a large city, has many attractions."""

# Training the tokenizer with sample text
tokenizer = PunktSentenceTokenizer(text)

# Tokenizing sentences
sentences = tokenizer.tokenize(text)

# Displaying the tokenized sentences
for sentence in sentences:
    print(sentence)
