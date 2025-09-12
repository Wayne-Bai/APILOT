import nltk
from nltk.tokenize import PunktSentenceTokenizer, sent_tokenize

nltk.download('punkt')

text = "Please generate python code with nltk to fulfill the purpose A sentence tokenizer which uses an unsupervised algorithm to build a model for abbreviation words, collocations, and words that start sentences; and then uses that model to find sentence boundaries. This approach has been shown to work well for many European languages."

tokenizer = PunktSentenceTokenizer()
sentences = tokenizer.tokenize(text)

print(sentences)
