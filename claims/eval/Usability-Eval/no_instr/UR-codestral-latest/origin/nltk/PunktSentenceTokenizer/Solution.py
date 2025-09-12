import nltk
from nltk.tokenize import PunktSentenceTokenizer

# Train a Punkt tokenizer.
corpus = '''
Place your text corpus here for training.
'''

tokenizer = PunktSentenceTokenizer()
tokenizer.train(corpus)  # This takes time.

# Now you can use the trained tokenizer.
text = "Put your text here."
sentences = tokenizer.tokenize(text)
print(sentences)
