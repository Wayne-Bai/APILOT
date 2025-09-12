import nltk
from nltk.tokenize import PunktSentenceTokenizer

# Download the Punkt tokenizer if it's not already downloaded
nltk.download('punkt')

# Sample text
text = "Your text here"

# Train the tokenizer on the text
tokenizer = PunktSentenceTokenizer(text)

# Use the tokenizer to get sentences
sentences = tokenizer.tokenize(text)
for sentence in sentences:
    print(sentence)
