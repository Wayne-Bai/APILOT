import nltk
from nltk.tokenize.punkt import PunktSentenceTokenizer

# Load the text
text = "This is a sample text. Dr. Smith comes from the U.K. He likes Python programming."

# Train the tokenizer on the text
tokenizer = PunktSentenceTokenizer()
tokenizer.train(text)

# Tokenize the text into sentences
sentences = tokenizer.tokenize(text)
print(sentences)
