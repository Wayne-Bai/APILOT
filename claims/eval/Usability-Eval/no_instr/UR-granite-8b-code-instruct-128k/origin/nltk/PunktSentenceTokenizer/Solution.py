import nltk
from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktTrainer

# Sample text to tokenize
text = "This is a sample sentence. This is another sample sentence. And this is yet another sample sentence."

# Create a sentence tokenizer using the Punkt algorithm
sentence_tokenizer = PunktSentenceTokenizer(text)

# Train the sentence tokenizer model using abbreviations, collocations, and sentence starters
trainer = PunktTrainer(sentence_tokenizer)
trainer.train(text)

# Find sentence boundaries using the trained sentence tokenizer
boundaries = sentence_tokenizer.get_sentence_boundaries(text)

# Print the sentence boundaries
print(boundaries)
