import spacy
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS
from typing import List
from etools.environment import *


def clean(document: str) -> str:
    """Prepare a document for input into a text mining process.

    Args:
        document: An e-mail represented as a single string object.
        
    Returns:
      A cleaned string. All characters that are not alphabetic or are
      considered as whitespace are removed. All alphabetic characters are set
      to lowercase. All words that are considered as stop words by Scikit-learn
      are removed.
    """
    document = document.lower()
    words = "".join(c for c in document if c.isalpha() or c.isspace()).split()
    return " ".join(w for w in words if w not in ENGLISH_STOP_WORDS)


def significant_words(document: str, words: int = 5) -> List[str]:
    """Return a list of the top *words* most significant words to *document*.
    
    Args:
        document: An e-mail represented as a single string object.
        words: An integer representing how many words to output.
    
    Returns:
        A list containing *words* number of words that characterize the
        document the best, according to the trained TF-IDF vectorizer.
        The lower the index of the word in the returned list, the more
        significant it is to *document*.
    """
    document = clean(document)
    vector   = TFIDF.transform([document]).toarray().flatten()
    pairs    = sorted(list(zip(vector, TFIDF.get_feature_names())))
    features = [feature for _, feature in pairs]
    try:
        return features[-words:][::-1]
    except IndexError as error:
        print("Error: words parameter greater than number of words.")
        return features[::-1]

        
def significant_sentences(document: str, sentences: int = 2) -> List[str]:
    """Return a list of the top *sentences* most significant sentences to
       *document*.
    
    Args:
        document: An e-mail represented as a single string object.
        sentences: An integer representing how many sentences to output.
    
    Returns:
        A list containing *sentences* number of sentences that characterize the
        document the best, according to the trained TF-IDF vectorizer.
        The lower the index of the sentence in the returned list, the more
        significant it is to *document*.
        
        This method tends to favor longer sentences, since longer sentences
        tend to provide more information.
    """
    sents  = [sent.string.strip() for sent in NLP(document).sents]
    scores = [TFIDF.transform([clean(sent)]).sum() for sent in sents]
    pairs  = sorted([(scores[i], sents[i]) for i in range(len(sents))])[::-1]
    significant_sents = [" ".join(sent.split()) for _, sent in pairs]
    try:
        return significant_sents[:sentences]
    except IndexError as error:
        print("Error: num_words parameter greater than number of words.")
        return significant_sents  


def summarizing_sentences(document: str, sentences: int = 2):
    """Return a list of the top *sentences* best summarizing sentences to
       *document*.
    
    Args:
        document: An e-mail represented as a single string object.
        sentences: An integer representing how many sentences to output.
    
    Returns:
        A list containing *sentences* number of sentences that summarize the
        document the best. These sentences contain the most words with a high
        degree of similarity to the other words in the document.
        The lower the index of the sentence in the returned list, the higher
        degree of representation it is to *document*.
    """
    counts = {}
    for word in NLP(clean(document)):
        counts[word.lemma_] = counts.get(word.lemma_, -1) + 1
    text   = NLP(document)
    sents  = [sent.string.strip() for sent in text.sents]
    scores = [0 for _ in sents]
    for i, sent in enumerate(text.sents):
        for word in NLP(clean(sent.string)):
            scores[i] += counts.get(word.lemma_, 0)         
    pairs = sorted([(scores[i], sents[i]) for i in range(len(sents))])[::-1]
    summarizing_sents = [" ".join(sent.split()) for _, sent in pairs]
    try:
        return summarizing_sents[:sentences]
    except IndexError as error:
        print("Error: num_words parameter greater than number of words.")
        return summarizing_sents
      