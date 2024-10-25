# Modified from: https://shariqhameed127.medium.com/named-entity-recognition-ner-nlp-basics-part-6-of-10-4cf3df102bf4
import nltk, spacy

def ner_nltk(text):
    entities = {}

    tokens = nltk.sent_tokenize(text)
    for sent in tokens:
        word_tokens = nltk.word_tokenize(sent)
        for i, chunk in enumerate(nltk.ne_chunk(nltk.pos_tag(word_tokens))):
            if hasattr(chunk, 'label'):
                entities[word_tokens[i]] = chunk.label()
                
    
    return entities

text = "Tesla opened a new office in Tokyo today"
print("NER with nltk")
print(ner_nltk(text))

def ner_spacy(sentence):
    nlp = spacy.load("en_core_web_sm")

    doc = nlp(sentence)

    named_entities = [token.ent_iob_ + "-" + token.ent_type_ for token in doc]
  
    return named_entities

print("NER with spacy")
print(ner_spacy("Tesla opened a new office in Tokyo today"))

