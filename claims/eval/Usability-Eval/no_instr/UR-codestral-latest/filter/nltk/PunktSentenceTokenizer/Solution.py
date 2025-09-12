# Import the necessary libraries
import nltk
from nltk.tokenize import PunktSentenceTokenizer

# Let's say we have some text
text = "Your text goes here."

# We initialize the tokenizer
tokenizer = PunktSentenceTokenizer()

# Now we can tokenize the text
sentences = tokenizer.tokenize(text)

# Print the sentences
for sentence in sentences:
    print(sentence)
