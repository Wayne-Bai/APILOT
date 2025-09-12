import nltk
from nltk.corpus import gutenberg
from nltk.tokenize import PunktSentenceTokenizer

# Download the required data if you haven't already
nltk.download('punkt')
nltk.download('gutenberg')

# Get text from a specific gutenberg book
# Let's use 'austen-emma.txt' for the demonstration
text = gutenberg.raw('austen-emma.txt')

# Train the sentence tokenizer
sentence_tokenizer = PunktSentenceTokenizer(text)

# Now we can use the trained tokenizer to split text into sentences
sentences = sentence_tokenizer.tokenize(text)

# Print out a few sentences to test
for i in range(5):
    print(f"Sentence {i+1}: {sentences[i]}")
