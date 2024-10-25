# Modified from: https://shariqhameed127.medium.com/removing-stop-words-nlp-basics-part-3-of-10-69ed1aeaac82

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def remove_stopwords(sentence):
    # Get the set of English stop words
    stop_words = set(stopwords.words('english'))
    
    # Tokenize the input sentence into words
    word_tokens = word_tokenize(sentence)

    # Filter out the stop words
    filtered_sentence = [word for word in word_tokens if word.lower() not in stop_words]

    # Return the filtered sentence as a string
    return ' '.join(filtered_sentence)

if __name__ == "__main__":
    print(stopwords.words('english'))

    # Sample sentence
    sample_sentence = "The quick brown fox jumps over the lazy dog."
    
    # Remove stop words from the sample sentence
    result = remove_stopwords(sample_sentence)
    
    # Print the result
    print("Original Sentence:", sample_sentence)
    print("Filtered Sentence:", result)
