import nltk
from nltk.tokenize import PunktSentenceTokenizer

# Sample text for demonstration
text = "Dr. Smith loves programming. He said, 'Let's build an awesome project!' It's amazing."

# Train a PunktSentenceTokenizer model
# For a real-world scenario, you may need a larger and more representative corpus
trainer = PunktSentenceTokenizer.train(text)
tokenizer = PunktSentenceTokenizer(trainer)

# Tokenize the text into sentences
sentences = tokenizer.tokenize(text)

# Output the results
for i, sentence in enumerate(sentences):
    print(f"Sentence {i + 1}: {sentence}")
