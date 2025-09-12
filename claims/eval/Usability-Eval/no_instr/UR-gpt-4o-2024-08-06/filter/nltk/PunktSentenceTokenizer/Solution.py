import nltk
from nltk.tokenize import PunktSentenceTokenizer
from nltk.corpus import gutenberg

# Download necessary NLTK data files
nltk.download('punkt')
nltk.download('gutenberg')

# Load a sample text from the Gutenberg corpus to train the tokenizer
train_text = gutenberg.raw('austen-emma.txt')

# Initialize an unsupervised sentence tokenizer
tokenizer = PunktSentenceTokenizer(train_text)

# Define a function to tokenize text into sentences
def tokenize_text(text):
    sentences = tokenizer.tokenize(text)
    return sentences

# Example usage
sample_text = "Mr. Smith bought a car yesterday. It cost $23,000! Isn't that amazing? Where did he buy it? He bought it at Smith's cars inc."

# Tokenize the sample text
tokenized_sentences = tokenize_text(sample_text)

# Print the tokenized sentences
for sentence in tokenized_sentences:
    print(sentence)
