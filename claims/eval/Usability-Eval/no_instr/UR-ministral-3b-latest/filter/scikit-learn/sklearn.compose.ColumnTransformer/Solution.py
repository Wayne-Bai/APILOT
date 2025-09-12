from transformers import BertTokenizer, BertModel

# Initialize the tokenizer and model
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

# Sample data
texts = ["This is a sample text.", "Another example sentence."]

# Tokenize the input texts
inputs = tokenizer(texts, return_tensors='pt', padding=True, truncation=True, max_length=128)

# Pass the inputs through the model
with torch.no_grad():
    outputs = model(**inputs)

# Print out the outputs
print(outputs)
