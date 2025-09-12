import nltk
from nltk.tokenize import PunktSentenceTokenizer

# Training the tokenizer
# Note that this uses an internal list of abbreviations, which may not cover all cases, especially for domain-specific jargon.
tokenizer = PunktSentenceTokenizer()

# Example text
text = "Your input text here."

# Tokenize the text into sentences
sentences = tokenizer.tokenize(text)

# Print the sentences
for sentence in sentences:
    print(sentence)
