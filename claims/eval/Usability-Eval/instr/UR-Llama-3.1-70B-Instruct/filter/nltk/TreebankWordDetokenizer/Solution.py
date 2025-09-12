import nltk
from nltk.tokenize.treebank import TreebankDetokenizer

# Ensure the required NLTK data is downloaded
nltk.download('punkt')

# Create a TreebankDetokenizer instance
detokenizer = TreebankDetokenizer()

# Tokenized text
tokenized_text = ["Hello", ",", "world", "!"]

# Detokenize the text
detokenized_text = detokenizer.detokenize(tokenized_text)

print(detokenized_text)  # Output: "Hello, world!"

# Another example with more complex text
tokenized_text = ["This", "is", "a", "test", ".", "It", "should", "detokenize", "correctly", "."]

detokenized_text = detokenizer.detokenize(tokenized_text)

print(detokenized_text)  # Output: "This is a test. It should detokenize correctly."
