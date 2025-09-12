import nltk
from nltk.tokenize import sent_tokenize

# Download the necessary resources. These resources help in tokenizing the sentences.
nltk.download('punkt')

# Sample text
text = "This is a sentence. Here's another one! Does this work well? It should: NLTK is quite powerful."

# Tokenize the text into sentences
sentences = sent_tokenize(text)

# Print the tokenized sentences
for i, sentence in enumerate(sentences, 1):
    print(f"Sentence {i}: {sentence}")
