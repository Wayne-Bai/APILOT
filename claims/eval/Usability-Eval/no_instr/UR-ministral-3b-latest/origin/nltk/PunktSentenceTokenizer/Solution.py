import nltk

# Download necessary packages if not already available
nltk.download('punkt')

from nltk.tokenize import TreebankWordTokenizer

tokenizer = TreebankWordTokenizer()

# Example sentences
sentences = [
    "Hello there, how are you today?",
    "I love using NLTK for text processing.",
    "Let's make a fantastic project together."
]

# Tokenize
tokenized_sentences = [tokenizer.tokenize(sentence) for sentence in sentences]

for i, tokens in enumerate(tokenized_sentences):
    print(f"Sentence {i + 1}: {tokens}")
