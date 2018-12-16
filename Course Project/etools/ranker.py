import spacy
import numpy as np
import pandas as pd
from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS
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


def unique(document: str) -> str:
    """Return a string of the unique words within a document.
    
    Args:
        document: An e-mail represented as a single string object.

    Returns:
        A string of space-separated sorted unique words from *document*.
    """
    document = clean(document)
    return " ".join(sorted(set(document.split())))


train = pd.concat([
    pd.read_excel("emails_300_set_1.xlsx", header=1),
    pd.read_excel("emails_300_set_2.xlsx", header=1),
])[["Content", "Important"]]
important   = [NLP(unique(d)) for d in train[train["Important"] == 1]["Content"]]
unimportant = [NLP(unique(d)) for d in train[train["Important"] == 0]["Content"]]


def score(document: str, emails = None) -> float:
    """Assign an importance score to this document between 0 and 1.
    
    Args:
        document: An e-mail represented as a single string object.
        emails: A list of spacy Language objects.
        
    Returns:
        A float value between 0 and 1. Documents that score close to 0 are very
        unimportant. Documents that score close to 1 are highly important.
        Essentially, this scoring metric outputs the average semantic
        similarity between the inputted document and the training set *train*
        of important documents.
    """
    emails = important if emails is None else emails
    nlp = NLP(clean(document))
    return np.max([nlp.similarity(email) for email in emails])
    

def is_important(document: str) -> bool:
    """Return True if this document is important. Return False otherwise.
    
    Args:
        document: An e-mail represented as a single string object.
        
    Returns:
        A boolean value. True if this document is important. False otherwise.
        Essentially, this function takes the semantic similarity between this
        document and the set of important documents and then compares that
        value with the semantic similarity between this document and the set of
        unimportant documents. If the document is more similar to the important
        e-mails, then the document is important. False otherwise.
    """
    return score(document, important) >= score(document, unimportant)
