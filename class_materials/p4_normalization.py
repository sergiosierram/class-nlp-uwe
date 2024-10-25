# Modified from: https://shariqhameed127.medium.com/text-normalization-nlp-basics-part-4-of-10-a2d15c3754dc

import contractions
import string

def lowercase_text(text):
    """
    This function takes text and returns the text in lowercase.
    """
    return text.lower()

punctuations = list(string.punctuation)

def remove_punctuations(text, punctuations):
    """
    This function removes punctuation from the text.
    """
    for punctuation in punctuations:
        text = text.replace(punctuation, '')
    return text.strip()

def expand_contractions(text):
    """
    This function expands contractions in the text.
    """
    expanded_text = []
    
    for word in text.split():
        expanded_text.append(contractions.fix(word))  
     
    expanded_text = ' '.join(expanded_text)
    return expanded_text

if __name__ == "__main__":
    # Sample text for processing
    sample_text = "It's a sunny day! Don't you think so? The quick brown fox jumps over the lazy dog."

    # Step 1: Expand contractions
    expanded_text = expand_contractions(sample_text)
    print("Expanded Text:", expanded_text)

    # Step 2: Remove punctuation
    text_no_punctuation = remove_punctuations(expanded_text, punctuations)
    print("Text without Punctuation:", text_no_punctuation)

    # Step 3: Convert to lowercase
    final_text = lowercase_text(text_no_punctuation)
    print("Final Lowercased Text:", final_text)
