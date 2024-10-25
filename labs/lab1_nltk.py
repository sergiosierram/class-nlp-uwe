import nltk
import spacy

# Download NLTK resources
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Sample text for processing
text = """AI isn't just a trend; it's reshaping the way we live and work. 
Companies can't ignore the benefits that come from using intelligent systems. 
If we embrace these changes, we'll unlock new opportunities for growth!"""

# NLTK Text Normalization, Tokenization, and POS Tagging
def nltk_processing(text):
    # Normalization (lowercase)
    normalized_text = text.lower()
    
    # Tokenization
    tokens = nltk.word_tokenize(normalized_text)
    
    # POS Tagging
    pos_tags = nltk.pos_tag(tokens)
    
    return tokens, pos_tags

# SpaCy Processing
def spacy_processing(text):
    # Load SpaCy model
    nlp = spacy.load("en_core_web_sm")
    
    # Process text with SpaCy
    doc = nlp(text)
    
    # Tokenization and POS tagging
    tokens = [token.text for token in doc]
    pos_tags = [(token.text, token.pos_) for token in doc]
    
    return tokens, pos_tags

# Run NLTK processing
nltk_tokens, nltk_pos_tags = nltk_processing(text)
print("NLTK Tokenization:")
print(nltk_tokens)
print("NLTK POS Tags:")
print(nltk_pos_tags)

# Run SpaCy processing
spacy_tokens, spacy_pos_tags = spacy_processing(text)
print("\nSpaCy Tokenization:")
print(spacy_tokens)
print("SpaCy POS Tags:")
print(spacy_pos_tags)
