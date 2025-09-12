import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

# Sample text for demonstration
text = "Dr. Smith goes to Paris. It's a beautiful city! However, Mr. Johnson believes otherwise. Don't you think?"

# Define a function for custom sentence tokenization
def custom_sentence_tokenizer(text):
    # Use NLTK's sent_tokenize method for initial sentence segmentation
    sentences = sent_tokenize(text)
    return sentences

# Tokenize the sample text into sentences
tokenized_sentences = custom_sentence_tokenizer(text)

# Print the tokenized sentences
for sentence in tokenized_sentences:
    print(sentence)
