from nltk.stem import WordNetLemmatizer
import spacy

# Load the SpaCy model for English
nlp = spacy.load('en_core_web_sm')

# Sample words for lemmatization
words = ["foxes", "jumping", "rocks", "corpora", "better"]

# Lemmatization using SpaCy
print("Lemmatization with SpaCy:")
for word in words:
    doc = nlp(word)
    lemmatized_spacy = [token.lemma_ for token in doc]
    print(f"{word}: {lemmatized_spacy[0]}")  # Output the lemmatized form

# Initialize the NLTK WordNet lemmatizer
lemmatizer = WordNetLemmatizer()

# Lemmatization using NLTK
print("\nLemmatization with NLTK:")
for word in words:
    # Specify part of speech for better lemmatization if necessary
    pos = "n" if word in ["rocks", "corpora"] else "v" if word == "jumping" else "a" if word == "better" else None
    lemmatized_nltk = lemmatizer.lemmatize(word, pos=pos) if pos else lemmatizer.lemmatize(word)
    print(f"{word}: {lemmatized_nltk}")
