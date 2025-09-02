from keras.preprocessing.text import Tokenizer

# Example sentences
sentences = ["I love deep learning", "I love machine learning"]

# Initialize and fit tokenizer
tokenizer = Tokenizer()
tokenizer.fit_on_texts(sentences)

# Print vocabulary and tokenized sequences
print("Vocabulary:", tokenizer.word_index)
print("Tokenized:", tokenizer.texts_to_sequences(sentences))
